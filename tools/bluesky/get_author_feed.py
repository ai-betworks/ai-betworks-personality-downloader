"""AI Agent tool wrapper to fetch Bluesky posts w/ Bluesky API. This is the main driver for gathering data from Bluesky.

Will fetch posts, then categorize them into:
- bluesky_posts
- bluesky_replies
  - Note: When a reply is encountered, follow up calls will be made to fetch the reply thread
- bluesky_reposts
  - Contains the post by the original author and the post that was reposted

Then will compress the data into a structured format (see models.py and converters.py for BlueskyPost, BlueskyReply, BlueskyRepost)
"""

from typing_extensions import List, Optional, Literal, Dict, TypedDict
import logging
from .models import BlueskyPost, BlueskyReply, BlueskyRepost
from .converters import convert_post
from .utils import create_client
from langgraph.types import Command
from langchain_core.tools import tool
from langchain_core.messages import ToolMessage
from langchain_core.tools.base import InjectedToolCallId
from typing_extensions import Any, Annotated
from .utils import dump_debug_file
import traceback


logger = logging.getLogger(__name__)


class PostParams(TypedDict):
    filter: Literal[
        "posts_with_replies",
        "posts_no_replies",
        "posts_with_media",
        "posts_and_author_threads",
    ]


def get_author_feed(
    tool_call_id: Annotated[str, InjectedToolCallId],
    handle: str,
    auth_handle: Optional[str] = None,
    auth_password: Optional[str] = None,
    limit: int = 1000,
    filter: str = "posts_with_replies",
    reply_depth: int = 1,
    debug: bool = True,
) -> Command:
    """Get recent posts from a Bluesky user and return them categorized by type.

    Args:
        tool_call_id (str): Unique identifier for this tool call, automatically injected by the framework
        handle (str): The user's Bluesky handle (e.g. 'example.bsky.social')
        auth_handle (Optional[str]): Handle for authentication if accessing private content
        auth_password (Optional[str]): Password for authentication if accessing private content
        limit (int): Maximum number of posts to fetch, defaults to 1000
        filter (str): Type of posts to include, one of: posts_with_replies, posts_no_replies, posts_with_media, posts_and_author_threads
        reply_depth (int): How many levels up the reply chain to fetch. Defaults to 1 (just the parent post)
        debug (bool): If True, dumps raw post data to a debug file for troubleshooting

    Returns:
        Command: A Command object containing:
            - bluesky_posts (Dict[str, BlueskyPost]): Regular posts keyed by URI
            - bluesky_replies (Dict[str, BlueskyReply]): Reply posts keyed by CID
            - bluesky_reposts (Dict[str, BlueskyRepost]): Reposted posts keyed by CID
            - messages (List[ToolMessage]): Status messages about the operation
    """
    # Validate filter parameter
    params: PostParams = {"filter": filter}  # type: ignore[typeddict-item]

    client = create_client(auth_handle, auth_password)
    posts_dict: Dict[str, BlueskyPost] = {}
    replies_dict: Dict[str, BlueskyReply] = {}
    reposts_dict: Dict[str, List[BlueskyRepost]] = {}
    cursor = None
    raw_responses = []
    error = None
    total_items = 0

    try:
        current_item = ""
        if not handle.endswith(".bsky.social"):
            handle = f"{handle}.bsky.social"
        while total_items < limit:
            print(f"fetching feed for {handle} with cursor {cursor}")
            response = client.get_author_feed(
                actor=handle,
                limit=min(100, limit - total_items),
                cursor=cursor,
                filter=params["filter"],
            )

            if debug:
                raw_responses.append(response.model_dump())

            for feed_item in response.feed:
                current_item = feed_item
                # Handle reposts
                if (
                    hasattr(feed_item, "reason")
                    and feed_item.reason
                    and feed_item.reason.py_type == "app.bsky.feed.defs#reasonRepost"
                ):
                    repost = BlueskyRepost(
                        repost_author={
                            "did": feed_item.post.author.did,
                            "handle": feed_item.post.author.handle,
                            "display_name": getattr(
                                feed_item.post.author, "display_name", None
                            ),
                            "description": getattr(
                                feed_item.post.author, "description", None
                            ),
                            "avatar_url": getattr(
                                feed_item.post.author, "avatar", None
                            ),
                        },
                        reposted_post=convert_post(feed_item.post),
                    )
                    reposts_dict[feed_item.post.uri] = repost
                    total_items += 1
                    continue

                post = convert_post(feed_item.post)

                # Handle replies - check record.reply instead of post.reply
                if (
                    feed_item.post.record
                    and hasattr(feed_item, "reply")
                    and feed_item.post.record.reply
                ):
                    reply = feed_item.post.record.reply
                    context_chain = []
                    current_uri = reply.parent.uri
                    depth = 0

                    # Load reply context chain up to specified depth
                    while current_uri is not None and depth < reply_depth:
                        context_response = client.get_posts(uris=[current_uri])
                        if debug:
                            raw_responses.append(context_response.model_dump())

                        if not context_response.posts:
                            break

                        context_post = context_response.posts[0]
                        converted_context_post = convert_post(context_post)
                        context_chain.append(converted_context_post)

                        # Get next parent URI if this post is a reply and we haven't hit depth limit
                        if (
                            depth + 1 < reply_depth
                            and hasattr(context_post.record, "reply")
                            and context_post.record.reply is not None
                        ):
                            current_uri = context_post.record.reply.parent.uri
                        else:
                            current_uri = None
                        depth += 1

                    replies_dict[feed_item.post.cid] = BlueskyReply(
                        post=post,
                        reply_to_parent=reply.parent.uri,
                        reply_to_root=(
                            reply.root.uri if hasattr(reply, "root") else None
                        ),
                        reply_context=context_chain,
                    )

                # Regular posts
                else:
                    posts_dict[feed_item.post.uri] = post

                total_items += 1

            cursor = response.cursor
            if not cursor or not response.feed:
                break
        return {
            "bluesky_posts": posts_dict,
            "bluesky_replies": replies_dict,
            "bluesky_reposts": reposts_dict,
        }

        # return Command(
        #     update={
        #         "bluesky_posts": posts_dict,
        #         # "bluesky_replies": replies_dict,
        #         # "bluesky_reposts": reposts_dict,
        #         "messages": [
        #             ToolMessage("Successfully fetched posts", tool_call_id=tool_call_id)
        #         ],
        #     }
        # )

    except Exception as e:
        logger.error("Full traceback:")
        logger.error(traceback.format_exc())
        print("Full traceback:")
        print(traceback.format_exc())
        logger.error(f"Error fetching posts for {handle}: {str(e)}")
        logger.error(f"Last item handled {current_item}")
        print(f"Error fetching posts for {handle}: {str(e)}")
        print(f"Last item handled {current_item}")
        raise

    finally:
        if debug:
            dump_debug_file(
                data=None,
                prefix="bluesky_posts",
                identifier=handle,
                raw_responses=raw_responses,
                processed_data=(
                    {
                        "bluesky_posts": posts_dict,
                        "bluesky_replies": replies_dict,
                        "bluesky_reposts": reposts_dict,
                    }
                    if total_items > 0
                    else None
                ),
            )
