"""TypedDicts for Bluesky data models"""

from typing_extensions import List, Optional, TypedDict, NotRequired, Union, Dict
from datetime import datetime


class BlueskyProfile(TypedDict):
    """TypedDict for Bluesky profile data"""

    did: str
    handle: str
    display_name: NotRequired[Optional[str]]
    description: NotRequired[Optional[str]]
    avatar_url: NotRequired[Optional[str]]
    followers_count: NotRequired[int]  # defaults to 0
    follows_count: NotRequired[int]  # defaults to 0
    posts_count: NotRequired[int]  # defaults to 0
    indexed_at: NotRequired[Optional[datetime]]


class AspectRatio(TypedDict):
    """TypedDict for media aspect ratio"""

    width: int
    height: int


class ImageEmbed(TypedDict):
    """TypedDict for image embeds"""

    alt: NotRequired[Optional[str]]
    fullsize: str
    thumb: str
    aspect_ratio: NotRequired[Optional[AspectRatio]]


class VideoEmbed(TypedDict):
    """TypedDict for video embeds"""

    alt: NotRequired[Optional[str]]
    thumbnail: str
    playlist: str
    aspect_ratio: NotRequired[Optional[AspectRatio]]


class ExternalEmbed(TypedDict):
    """TypedDict for external link embeds"""

    uri: str
    title: str
    description: str
    thumb: NotRequired[Optional[str]]


class RecordEmbed(TypedDict):
    """TypedDict for embedded record (e.g. quoted post)"""

    uri: str
    cid: NotRequired[str]
    author_did: NotRequired[str]  # For feed posts
    author_handle: NotRequired[str]  # For feed posts
    text: NotRequired[str]  # For feed posts
    value: NotRequired[dict]  # The actual record data for non-feed posts
    labels: NotRequired[List[str]]
    embeds: NotRequired[List[Union[ImageEmbed, VideoEmbed, ExternalEmbed]]]


class RecordWithMediaEmbed(TypedDict):
    """TypedDict for record with media embed"""

    record: RecordEmbed
    media: Union[ImageEmbed, VideoEmbed]


class BlueskyPost(TypedDict):
    """TypedDict for a Bluesky post"""

    uri: str
    cid: str
    author_did: str
    author_handle: str
    text: str
    created_at: datetime
    indexed_at: datetime
    reply_count: NotRequired[int]  # defaults to 0
    repost_count: NotRequired[int]  # defaults to 0
    like_count: NotRequired[int]  # defaults to 0
    quote_count: NotRequired[int]  # defaults to 0
    reply_to_parent: NotRequired[
        Optional[str]
    ]  # URI of the parent post if this is a reply
    reply_to_root: NotRequired[Optional[str]]  # URI of the root post if this is a reply
    parent_post: NotRequired[Optional["BlueskyPost"]]
    root_post: NotRequired[Optional["BlueskyPost"]]
    embed: NotRequired[
        Optional[
            Union[
                List[ImageEmbed],  # For multiple images
                ImageEmbed,  # For single image
                VideoEmbed,  # For video
                ExternalEmbed,  # For external links
                RecordEmbed,  # For quoted posts
                RecordWithMediaEmbed,  # For quoted posts with media
            ]
        ]
    ]


class BlueskyThread(TypedDict):
    """TypedDict for a Bluesky thread"""

    post: BlueskyPost
    parent_posts: NotRequired[List[BlueskyPost]]  # defaults to empty list
    replies: NotRequired[List[BlueskyPost]]  # defaults to empty list


class BlueskyReply(TypedDict):
    """TypedDict for a Bluesky reply"""

    post: BlueskyPost
    reply_to_parent: str  # URI of the parent post
    reply_to_root: Optional[str]  # URI of the root post if different from parent
    reply_context: List[BlueskyPost]  # Posts leading up to this reply


class BlueskyRepost(TypedDict):
    """TypedDict for a Bluesky repost"""

    repost_author: BlueskyProfile  # The user who reposted
    reposted_post: BlueskyPost  # The original post that was reposted


class BlueskyPostsResponse(TypedDict):
    """TypedDict for the response from get_user_posts"""

    bluesky_posts: Dict[str, BlueskyPost]  # URI -> Post mapping
    bluesky_replies: Dict[str, BlueskyReply]  # CID -> Reply mapping
    bluesky_reposts: Dict[
        str, List[BlueskyRepost]
    ]  # Author DID -> List of their reposts
