from typing import Annotated

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_community.document_loaders import WikipediaLoader
from langchain_community.tools import TavilySearchResults
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import END, START, MessagesState, StateGraph
from tools.bluesky.get_author_feed import get_author_feed
from tools.bluesky.get_profile import get_profile
from tools.bluesky.utils import reduce_bluesky_posts, reduce_bluesky_replies
from tools.common import reduce_dict_merge
from models import MasterResearchDict, SearchQueries, SearchQuery, SocialInfo
import os
import uuid

load_dotenv()


# Parent state for all steps
class ResearchGraphOutput(MessagesState):
    research: Annotated[MasterResearchDict, reduce_dict_merge]


llm = ChatAnthropic(
    model="claude-3-5-haiku-20241022",
    # model="claude-3-5-sonnet-20241022",
    temperature=0,
)


# First use an LLM to prepare search queries for the public figure's social media pages
# Then use Tavily to search the web for the social media pages
def search_web_for_socials(state: ResearchGraphOutput):
    """Retrieve docs from web search"""

    print("Preparing search queries for social media pages")

    social_finder_sys_msg = SystemMessage(
        content="""
    You will be given the name of a public figure.

    Your goal is to form well structured web search queries to find social media pages belonging to the public figure:
    - The public figure's BlueSky page
    - The public figure's Facebook page
    - The public figure's X page. Do not refer to it as Twitter or reference Twitter in your search query.
    - The public figure's Instagram page
    - The public figure's LinkedIn page
    - The public figure's TikTok page
    - The public figure's YouTube page
    - The public figure's Truth Social page

    Respond with the search queries in a list, and nothing else.
    """
    )

    # Search
    tavily_search = TavilySearchResults(max_results=5)

    # Search query
    # TODO handle 429
    structured_llm = llm.with_structured_output(SearchQueries)
    social_search_queries = structured_llm.invoke(
        [social_finder_sys_msg] + state["messages"]
    )

    all_search_docs = []

    # search_queries is a string containing a list: '["a", "b", "c"]', this converts it to a list by evaluating the string as though it were code
    print(
        "type of social_search_queries.search_queries",
        type(social_search_queries.search_queries),
    )
    for query in social_search_queries.search_queries:
        print(f"Searching for {query}")
        search_docs = tavily_search.invoke(query)
        all_search_docs.extend(search_docs)

    # Format
    formatted_search_docs = "\n\n---\n\n".join(
        [
            f'<Document href="{doc["url"]}"/>\n{doc["content"]}\n</Document>'
            for doc in all_search_docs
        ]
    )
    print("tavily search results:", formatted_search_docs)
    return {"research": {"social_search_results": formatted_search_docs}}


# Take the search results from Tavily and use an LLM to extract the URLs and usernames for the user's socials
def extract_social_urls(state: ResearchGraphOutput):
    """Node to extract a figure's socials from search results"""

    print("Extracting social URLs from search results")

    answer_sys_msg = """
    You will be given search results from the web containing links to socials for a public figure.

    Here's a list of search results for the public figure's socials:
    {search_results}

    Your goal is to analyze the search results and to answer the following questions:
    1. What is the public figure's BlueSky page?
    2. What is the public figure's BlueSky handle?
    3. What is the public figure's Facebook page?
    4. What is the public figure's Facebook username?
    5. What is the public figure's X page?
    6. What is the public figure's X handle?
    7. What is the public figure's Instagram page?
    8. What is the public figure's Instagram username?
    9. What is the public figure's LinkedIn page?
    10. What is the public figure's LinkedIn username?
    11. What is the public figure's TikTok page?
    12. What is the public figure's TikTok username?
    13. What is the public figure's YouTube page?
    14. What is the public figure's YouTube username?
    15. What is the public figure's Truth Social page?
    16. What is the public figure's Truth Social username?

    Note the following (PROFILE_HANDLE is a placeholder for the public figure's handle or username):
    - BlueSky urls often look like this: https://bsky.app/profile/(PROFILE_HANDLE).bsky.social. 
    - Facebook urls often look like this: https://www.facebook.com/(PROFILE_HANDLE)
    - X urls often look like this: https://x.com/(PROFILE_HANDLE)
    - YouTube urls often look like this: https://www.youtube.com/@(PROFILE_HANDLE)
    - Instagram urls often look like this: https://www.instagram.com/(PROFILE_HANDLE)
    - LinkedIn urls often look like this: https://www.linkedin.com/in/(PROFILE_HANDLE)
    - TikTok urls often look like this: https://www.tiktok.com/@(PROFILE_HANDLE)
    - Truth Social urls often look like this: https://truthsocial.com/(PROFILE_HANDLE)

    Respond to this question in a JSON object with the following keys:
    - bluesky_page
    - bluesky_handle
    - facebook_page
    - facebook_username
    - twitter_page
    - twitter_handle
    - instagram_page
    - instagram_username
    - linkedin_page
    - linkedin_username
    - tiktok_page
    - tiktok_username
    - youtube_page
    - youtube_username
    - truth_social_page
    - truth_social_username

    If you could not find the infomation for any of the questions, then the key should be present in the object, but with an empty string as the value.
    """

    social_search_results = state.get("research", {}).get("social_search_results")

    formatted_answer_sys_msg = SystemMessage(
        content=answer_sys_msg.format(search_results=social_search_results)
    )

    social_gatherer = llm.with_structured_output(SocialInfo)
    extracted_socials = social_gatherer.invoke(
        [formatted_answer_sys_msg] + state["messages"]
    )

    print(extracted_socials)
    return {"research": {"socials": extracted_socials}}


# Taking the BlueSky URL that we got from the Tavily Search results, get their BlueSky profile from the API
def scrape_blue_sky_profile(state: ResearchGraphOutput):
    """Scrape Blue Sky profile"""

    print("Scraping Blue Sky profile")
    socials = state.get("research", {}).get("socials")

    if not socials or not socials.bluesky_handle:
        return {"research": {"bluesky_profile": None}}

    profile = get_profile(
        uuid.uuid4(),
        socials.bluesky_handle,
        auth_handle=os.getenv("BLUESKY_HANDLE"),
        auth_password=os.getenv("BLUESKY_PASSWORD"),
        debug=True,
    )

    return {"research": {"bluesky_profile": profile}}


# Take the BlueSky profile and get their last 100 posts, replies, and reposts
def scrape_blue_sky_posts(state: ResearchGraphOutput):
    """Scrape Blue Sky posts"""

    print("Scraping Blue Sky posts")

    socials = state.get("research", {}).get("socials")

    if not socials or not socials.bluesky_handle:
        return {
            "research": {
                "bluesky_posts": [],
                "bluesky_replies": [],
                "bluesky_reposts": [],
            }
        }

    posts = get_author_feed(
        uuid.uuid4(),  # Tool call id, this is made up right now but needs to be fixed later
        socials.bluesky_handle,
        auth_handle=os.getenv("BLUESKY_HANDLE"),
        auth_password=os.getenv("BLUESKY_PASSWORD"),
        limit=10,  # TODO Change to 100
        filter="posts_with_replies",
        reply_depth=1,
        debug=True,
    )

    return {
        "research": {
            "bluesky_posts": [v for v in posts["bluesky_posts"].values()],
            "bluesky_replies": [v for v in posts["bluesky_replies"].values()],
            "bluesky_reposts": [v for v in posts["bluesky_reposts"].values()],
        }
    }


def search_wikipedia(state: ResearchGraphOutput):
    """Retrieve docs from wikipedia"""

    # Search query writing
    search_instructions = SystemMessage(
        content=f"""You will be given the name of a public figure. 

    Your goal is to generate a well-structured query to find Wikipedia pages relevant to the public figure.
    
    Take the name of the public figure and return a well structured query that can be used to search for Wikipedia pages relevant to the public figure"""
    )

    # Search query
    structured_llm = llm.with_structured_output(SearchQuery)
    search_query = structured_llm.invoke([search_instructions] + state["messages"])
    print("Wikipedia search query:", search_query.search_query)
    # Search
    search_docs = WikipediaLoader(
        query=search_query.search_query, load_max_docs=2
    ).load()
    print("Wikipedia search results:", search_docs)

    formatted_search_docs = []
    for doc in search_docs:
        # Format
        formatted_search_doc = f'<Document source="{doc.metadata["source"]}" page="{doc.metadata.get("page", "")}"/>\n{doc.page_content}\n</Document>'
        formatted_search_docs.append(formatted_search_doc)

    return {
        "research": {
            "wikipedia_search_results": formatted_search_docs,
        }
    }


research_graph_builder = StateGraph(ResearchGraphOutput)
research_graph_builder.add_node("search_web_for_socials", search_web_for_socials)
research_graph_builder.add_node("extract_social_info", extract_social_urls)
research_graph_builder.add_node("scrape_blue_sky_profile", scrape_blue_sky_profile)
research_graph_builder.add_node("scrape_blue_sky_posts", scrape_blue_sky_posts)
research_graph_builder.add_node("search_wikipedia", search_wikipedia)

# Flow
research_graph_builder.add_edge(START, "search_web_for_socials")
research_graph_builder.add_edge(START, "search_wikipedia")

research_graph_builder.add_edge("search_web_for_socials", "extract_social_info")
# social_graph_builder.add_edge("extract_social_info", END)
research_graph_builder.add_edge("extract_social_info", "scrape_blue_sky_profile")
research_graph_builder.add_edge("extract_social_info", "scrape_blue_sky_posts")
research_graph_builder.add_edge("scrape_blue_sky_profile", END)
research_graph_builder.add_edge("scrape_blue_sky_posts", END)
research_graph_builder.add_edge("search_wikipedia", END)

research_agent = research_graph_builder.compile()
