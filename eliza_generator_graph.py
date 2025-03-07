from typing import Annotated, List, TypedDict, Literal, Union, Dict
from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel
from tools.bluesky.utils import (
    reduce_bluesky_posts,
    reduce_bluesky_replies,
    format_replies_as_xml,
)
from tools.common import default_llm, reduce_dict_merge

from models import ElizaDict, ElizaRawDict
from research_graph import MasterResearchDict
from pprint import pprint
from typing import Any


# TODO, later we will want to fetch many articles and gradually use llms to summarize and merge. Relatively few models have a context window that could handle multiple articles
class ElizaBioOutput(BaseModel):
    events: list[dict[str, str]]


class ElizaStyleOutput(BaseModel):
    style: dict
    adjectives: list[str]


class ElizaTopicsKnowledgeOutput(BaseModel):
    topics: List[str]  # List of topic strings
    knowledge: List[str]  # List of knowledge items


class MessageContent(BaseModel):
    text: str


class Message(BaseModel):
    user: str
    content: MessageContent


class ElizaRealPostExamplesOutput(BaseModel):
    messageExamples: List[
        List[Dict[Literal["user", "content"], Union[str, Dict[Literal["text"], str]]]]
    ]
    postExamples: List[str]


class BotGeneratorOutputState(TypedDict):
    public_figure: str
    research: Annotated[
        MasterResearchDict, reduce_dict_merge
    ]  # Nothing is changing research, need to debug why I need this
    raw: Annotated[ElizaRawDict, reduce_dict_merge]
    eliza: Annotated[ElizaDict, reduce_dict_merge]


def generate_bio(state: BotGeneratorOutputState):
    # Helper text from Autonome - BIO: "Provide a detailed biography of the character, including their background, life experiences, and key personality traits. Write one complete sentence per line."
    # Below JSON output has redundant fields for CoT and early debugging, you should only store the biography in state
    bio_prompt = """
    You are a world class biographer who has written biographies for many public figures.

    Your goal is to write a specially formatted biography for: {public_figure}

    You have been given the following articles:
    {articles}

    Do the following:
    1. Analyze the resources you have been given and identify major life events and experiences that the public figure has had.
    2. Identify how those experiences have shaped the public figure's personality and world view
    3. Write a biography of this person that summarizes their life and key personality traits in 500 words or less. Make sure that the biography is coherent, does the order of events make sense, do they really enforce {public_figure}'s personality? Each sentence should only contain one individual event.
    4. Finally, respond with a JSON object containing the following keys and nothing else:
    ```json
    {{
        "public_figure": string, // The name of the public figure, used to reinforce the fact that you are writing a bio
        "events": [{{
                "timerange": string, // The time range or date for the event. Use an exact date if possible, otherwise use a time range.
                "event": string, // A single sentence describing the event, no sentence is allowed to be longer than 40 words. 
                "source": string, //snippets of text where you found the event
        }}],
    }}
    ```
    """

    research = state.get("research")
    if not research:
        print("Can't generate bio without research")
        return {"raw": {"events": []}, "eliza": {"events": []}}

    wikipedia_search_results = research.get("wikipedia_search_results")
    if not wikipedia_search_results:
        print("Can't generate bio without wikipedia search results")
        return {"raw": {"events": []}, "eliza": {"events": []}}

    public_figure = state.get("public_figure")
    if not public_figure:
        print("Can't generate bio without public_figure")
        return {"raw": {"events": []}, "eliza": {"events": []}}

    prompt = bio_prompt.format(
        public_figure=public_figure, articles=wikipedia_search_results
    )

    # Search query
    structured_llm = default_llm().with_structured_output(ElizaBioOutput)
    search_query = structured_llm.invoke([prompt])
    print(search_query)
    return {
        "raw": {"events": search_query.events},
        "eliza": {"events": [event["event"] for event in search_query.events]},
    }


def generate_topics_knowledge(state: BotGeneratorOutputState):
    # TODO: Including knowledge here is just to save time
    # TODO: Don't hardcode bluesky and wikipedia, make it dynamic
    topics_prompt = """ 
    You are a Market Analyst who has been tracking a public figure, {public_figure}'s, socials and online presence for several years.

    You will be given a set of BlueSkey posts and some Wikipedia pages about the public figure. Your goal is to consolidate information from these sources into a specially formatted summary of the public figure's online presence.

    These are the sources you have been given. 
    ```json
    {{
        "wikipedia_search_results": {wikipedia_search_results}
        "bluesky_posts": {bluesky_posts}
        "bluesky_replies": {bluesky_replies}
    }}
    ```
        
    Do the following:
    1. Read the social media sources and identify what topics the public figure frequently discusses and areas where they seem to have expertise.
    2. Read the reposts and replies and identify what topics the public figure frequently engages in
    3. Cross reference your findings against the Wikipedia pages to see if the public figure's topics align with their life experiences. You can include elements that aren't present in wikipedia in your response, but you should add weight to elements that align.
    4. Finally return a JSON object with the following keys and nothing else:
    ```json
    {{
        "public_figure": string, // The name of the public figure, used to reinforce the fact that you are writing a topics analysis
        "topics": string[], // Topics that the public figure frequently discusses and engages in
        "knowledge": [], // Things that the public figure knows
    }}
    ```
    """

    research = state.get("research")
    if not research:
        print("Can't generate topics without research")
        return {"raw": {"topics": []}, "eliza": {"topics": []}}
    print("TOPICS", pprint(research))

    reduced_posts = reduce_bluesky_posts(research.get("bluesky_posts", []))
    reduced_replies = reduce_bluesky_replies(research.get("bluesky_replies", []))

    prompt = topics_prompt.format(
        public_figure=state.get("public_figure"),
        wikipedia_search_results=research.get("wikipedia_search_results", []),
        bluesky_posts=reduced_posts,
        bluesky_replies=reduced_replies,
    )

    structured_llm = default_llm().with_structured_output(ElizaTopicsKnowledgeOutput)
    search_query = structured_llm.invoke([prompt])
    print(search_query)

    return {
        "raw": {
            "topics": search_query.topics,
            "knowledge": search_query.knowledge,
        },
        "eliza": {
            "topics": search_query.topics,
            "knowledge": search_query.knowledge,
        },
    }


def generate_style_adjectives(state: BotGeneratorOutputState):
    # TODO Linguist is not the best specialist for personality, I think that's a speech pathologist, I just have it here to save time for now.
    style_prompt = """
    You are a sociolinguist tasks with analyzing the speech patterns of a public figure, {public_figure}, on social media. 

    You will be given a set of short and long form posts (referred to as "posts" below), as well as examples of conversations between the public figure and others (referred to as "conversations" below).

    Your goal is to analyze how the public figure speaks, and then to write a brief list of the key characteristics of that person's speech, as well as any speech patterns the speaker may have.

    Here are the sources you have been given and what form of content each source contains. If a source has no examples, it means that the public figure does not have a public social presence on that site, and you can omit it from your analysis:
    ```json
    {{
        "bluesky_posts": {{
            "style": "posts",
            "examples": {bluesky_posts}
        }},
        "bluesky_replies": {{
            "style": "conversations",
            "examples": {bluesky_replies}
        }}
    }}
    ```

    Do the following:
    1. Analyze all short and long form posts from the user and identify the tone and style of their posts. Figure out aspects of their speech like if they're formal or informal, if their speech is stiff or emotional, and other key characterstics of their speech. Also identify common content that they include in their messages, for instance, are they typically trying to inform the audience of their personal life or the news, are they posting tips and tricks, and so on.
    2. Analyze all conversations between the user and others. What tone do they take with others, for example, are they polite or aggressive, are they friendy or distant, etc. Identify what topics typically come up in conversations this person participates in.
    3. Based on the speech patterns of the individual, identify what personality traits the individual has.
    4. Finally, take all of your findings and summarize them into a JSON object with the following keys and nothing else:
    ```json
    {{  
        "public_figure": string, // The name of the public figure, used to reinforce that you are writing a style analysis
        "style": {{
            "all": string[], // A list of common aspects of the public figure's speech across both posts and conversations
            "chat": string[], // A list of common aspects of the public figure's speech in conversations
            "post": string[], // A list of common aspects of the public figure's speech in posts
        }},
        "adjectives": string[] // A list of personality traits that you have identified by analyzing the public figure's speech
    }}
    ```
    """
    research = state.get("research")
    if not research:
        print("Can't generate style without research")
        return {
            "raw": {"style": {}, "adjectives": []},
            "eliza": {"style": {}, "adjectives": []},
        }
    print("STYLE", pprint(research))

    reduced_posts = reduce_bluesky_posts(research.get("bluesky_posts"))
    reduced_replies = reduce_bluesky_replies(research.get("bluesky_replies"))

    prompt = style_prompt.format(
        public_figure=state.get("public_figure"),
        bluesky_posts=reduced_posts,
        bluesky_replies=reduced_replies,
    )
    structured_llm = default_llm().with_structured_output(ElizaStyleOutput)
    search_query = structured_llm.invoke([prompt])

    print("search query: ", search_query)
    return {
        "raw": {
            "style": search_query.style.get(
                "style"
            ),  # TODO Some bug w/ output, LLM JSON output might have unintentional nesting
            "adjectives": search_query.style.get("adjectives"),
        },
        "eliza": {
            "style": search_query.style.get(
                "style"
            ),  # TODO Some bug w/ output, LLM JSON output might have unintentional nesting
            "adjectives": search_query.style.get("adjectives"),
        },
    }


def generate_real_post_examples(state: BotGeneratorOutputState):
    # Debug dump of state
    print("\n=== DEBUG STATE DUMP ===")
    print(state)
    print("=== END DEBUG DUMP ===\n")
    public_figure = state.get("public_figure")
    research = state.get("research")
    eliza = state.get("eliza")

    if not public_figure:
        print("Can't get real post examples without public figure")
        return {"postExamples": [], "messageExamples": []}

    if not research:
        print("Can't get real post examples without research")
        return {"postExamples": [], "messageExamples": []}

    if not state.get("eliza"):
        print("Can't confidently generate real post examples without eliza")
        return {"postExamples": [], "messageExamples": []}

    style = eliza.get("style")
    topics = eliza.get("topics")
    knowledge = eliza.get("knowledge")
    adjectives = eliza.get("adjectives")
    reduced_posts = reduce_bluesky_posts(research.get("bluesky_posts"))
    reduced_replies = reduce_bluesky_replies(research.get("bluesky_replies"))
    formatted_replies = format_replies_as_xml(reduced_replies)
    handles = research.get("socials")
    print("handles", handles)
    print("topics", topics)
    print("knowledge", knowledge)
    print("adjectives", adjectives)
    print("style", style)
    print("style['post']", style["post"])
    print("bluesky_posts", reduced_posts)
    print("bluesky_replies", formatted_replies)

    message_examples_prompt = """You are a journalist who is writing a profile on {public_figure}
    
    Here is a list of posts from {public_figure}'s social media:
    <posts>
        {bluesky_posts}
    </posts>

    Here is a list of conversations {public_figure} has had with others on social media in JSON format. Each element in the array represents a conversation thread, each conversation thread is an array of messages where the speaker is identified by the "speaker" key and the text of their message is identified by the "text" key:
    <replies>
        {bluesky_replies}
    </replies>
    
    Here are the public figure's social media handles. You can use these to identify when {public_figure} is speaking in the posts and conversations in addition to their name:
    <handles>
        {handles}
    </handles>
    
    Here is a list of topics {public_figure} frequently discusses and engages in:
    <topics>
        {topics}
    </topics>

    Here is a list of things {public_figure} knows:
    <knowledge>
        {knowledge}
    </knowledge>

    Here is a list of personality traits that {public_figure} has:
    <adjectives>
        {adjectives}
    </adjectives>

    Here is a list of common aspects of {public_figure}'s speech across posts:
    <post_speech_style>
        {style_post}
    </post_speech_style>
    
    Here is a list of common aspects of {public_figure}'s speech across conversations:
    <chat_speech_style>
        {style_chat}
    </chat_speech_style>
    
    Here is a list of common aspects of {public_figure}'s speech across both posts and conversations:
    <all_speech_style>
        {style_all}
    </all_speech_style>

    Your goal is to identify which posts and conversations are most representative of the public figure's speech patterns. You will do the following:
    1. First read the lists that describe the public figure's speech style, topics, knowledge, and personality.
    2. Then read the posts and conversations, and create a short list of which ones are most representative of the public figure's speech patterns.
    3. Then look at the short list of posts and conversations, and identify which ones are most representative of the public figure, reducing the list to at least 5 (if able) and at most 10 examples of posts and at least 5 (if able) and at most 10 examples of conversations.
    4. Finally return a list of the unaltered posts and replies that are most representative of the public figure in the following format. You should return at most 5 examples and your response should only consist of the JSON object described below and nothing else:
    ```json
    {{ 
        postExamples: string[], // A list of the unaltered posts that are most representative of the public figure
        messageExamples: [[{{ // An array of reply threads, where each reply thread is an array of messages between the public figure and others. So your result should be an array of arrays of messages
          user: string, //The speaker of the message, which should be the name of the public figure and not the handle
          content: {{
            text: string, // The unaltered text of the message in the reply thread
        }}
        }}]]
    }}
    ```
    """
    prompt = message_examples_prompt.format(
        public_figure=state.get("public_figure"),
        bluesky_posts=reduced_posts,
        bluesky_replies=formatted_replies,
        handles=handles,
        topics=topics,
        knowledge=knowledge,
        adjectives=adjectives,
        style_post=style["post"],
        style_chat=style["chat"],
        style_all=style["all"],
    )
    # First get the raw JSON response from the LLM
    raw_response = default_llm().invoke([prompt])
    print("Raw LLM response:", raw_response)

    structured_llm = default_llm().with_structured_output(ElizaRealPostExamplesOutput)
    res = structured_llm.invoke([prompt])

    print("examples res", res)
    pprint(res.postExamples)
    print("message examples", res.messageExamples)
    pprint(type(res.messageExamples))

    return {
        "eliza": {
            "postExamples": res.postExamples,
            "messageExamples": res.messageExamples,
        }
    }


# Add nodes and edges
eliza_generator_builder = StateGraph(BotGeneratorOutputState)
eliza_generator_builder.add_node("generate_bio", generate_bio)
eliza_generator_builder.add_node("generate_topics_knowledge", generate_topics_knowledge)
eliza_generator_builder.add_node("generate_style_adjectives", generate_style_adjectives)
eliza_generator_builder.add_node(
    "generate_real_post_examples", generate_real_post_examples
)

# Logic
eliza_generator_builder.add_edge(START, "generate_bio")
eliza_generator_builder.add_edge(START, "generate_topics_knowledge")
eliza_generator_builder.add_edge(START, "generate_style_adjectives")

eliza_generator_builder.add_edge(
    ["generate_bio", "generate_topics_knowledge", "generate_style_adjectives"],
    "generate_real_post_examples",
)
eliza_generator_builder.add_edge("generate_real_post_examples", END)

eliza_generator_agent = eliza_generator_builder.compile()
