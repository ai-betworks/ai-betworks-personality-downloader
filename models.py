from typing import Annotated, List, Dict, Literal, TypedDict, Union
from langgraph.graph import MessagesState
from pydantic import BaseModel, Field
from tools.bluesky.models import (
    BlueskyPost,
    BlueskyProfile,
    BlueskyReply,
    BlueskyRepost,
)
from tools.common import reduce_dict_merge


class ElizaStyleDict(TypedDict):
    all: List[str]  # Common aspects of speech across posts and conversations
    chat: List[str]  # Common aspects of speech in conversations
    post: List[str]  # Common aspects of speech in posts


# Raw sometimes has extra fields, but we don't want to store them in state
class ElizaRawDict(TypedDict):
    events: List[
        Dict[str, str]
    ]  # List of dicts with timerange, event, and source fields
    topics: List[
        Dict[str, str]
    ]  # List of dicts with topic and supporting_sources fields
    knowledge: List[str]  # Things that the public figure knows
    style: ElizaStyleDict
    adjectives: List[str]  # Personality traits identified from speech analysis


# TODO, there has to be a type from Eliza we can import
# TODO, I'm using camel case here to get the right JSON output at the end, but mixed variable casing across the codebase is irritating
class ElizaDict(TypedDict):
    events: List[str]  # Events as a list of strings (raw.events.event)
    topics: List[str]  # Topics as a list of strings (raw.topics.topic)
    knowledge: List[str]  # Things that the public figure knows (raw.knowledge)
    style: ElizaStyleDict
    adjectives: List[str]  # Personality traits identified from speech analysis
    messageExamples: List[
        List[Dict[Literal["user", "content"], Union[str, Dict[Literal["text"], str]]]]
    ]
    postExamples: List[str]
    clients: List[str]  # Hardcoded at end
    modelProvider: str  # Hardcoded at end
    plugins: List[str]  # Hardcoded at end


class SocialInfo(BaseModel):
    bluesky_page: str = Field(None, description="The public figure's BlueSky page.")
    bluesky_handle: str = Field(None, description="The public figure's BlueSky handle.")
    facebook_page: str = Field(None, description="The public figure's Facebook page.")
    facebook_username: str = Field(
        None, description="The public figure's Facebook username."
    )
    x_page: str = Field(None, description="The public figure's X page.")
    x_username: str = Field(None, description="The public figure's X username.")
    instagram_page: str = Field(None, description="The public figure's Instagram page.")
    instagram_username: str = Field(
        None, description="The public figure's Instagram username."
    )
    linkedin_page: str = Field(None, description="The public figure's LinkedIn page.")
    linkedin_username: str = Field(
        None, description="The public figure's LinkedIn username."
    )
    tiktok_page: str = Field(None, description="The public figure's TikTok page.")
    tiktok_username: str = Field(
        None, description="The public figure's TikTok username."
    )
    youtube_page: str = Field(None, description="The public figure's YouTube page.")
    youtube_username: str = Field(
        None, description="The public figure's YouTube username."
    )
    truth_social_page: str = Field(
        None, description="The public figure's Truth Social page."
    )
    truth_social_username: str = Field(
        None, description="The public figure's Truth Social username."
    )


class MasterResearchDict(TypedDict):
    social_search_queries: list[str]  # Search queries for figure's social
    socials: SocialInfo  # Social info
    bluesky_profile: BlueskyProfile  # Blue Sky profile
    bluesky_posts: list[BlueskyPost]  # Blue Sky posts
    bluesky_replies: list[BlueskyReply]  # Blue Sky replies
    bluesky_reposts: list[BlueskyRepost]  # Blue Sky reposts
    wikipedia_search_query: str  # Wikipedia search query
    wikipedia_search_results: list[str]  # Search results from wikipedia
    article_search_queries: list[str]  # Article search queries
    blog_posts: list[str]  # Blog posts
    interviews: list[str]  # Search results from interviews
    articles: list[str]  # Articles
    opeds: list[str]  # Op-eds
    interviews: list[str]  # Interviews
    video_transcripts: list[str]  # Video transcripts


class DeploymentDict(TypedDict):
    target_platform: str
    endpoint: str
    success: bool
    raw_output: str


class MasterState(MessagesState):
    public_figure: str
    fictional: bool
    research: Annotated[MasterResearchDict, reduce_dict_merge]
    raw: Annotated[ElizaRawDict, reduce_dict_merge]
    eliza: Annotated[ElizaDict, reduce_dict_merge]
    deployment: Annotated[DeploymentDict, reduce_dict_merge]


# Used in 1.1.1 (social links) and 1.3.1 (articles)
class SearchQuery(BaseModel):
    search_query: str = Field("", description="Single search query.")


class SearchQueries(BaseModel):
    search_queries: list[str] = Field(None, description="Search queries for retrieval.")
