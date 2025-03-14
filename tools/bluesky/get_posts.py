"""AI Agent tool wrapper to fetch one or more Bluesky posts w/ Bluesky API"""
from typing_extensions import List, Optional, Dict
from langchain_core.messages import ToolMessage
from langchain_core.tools.base import InjectedToolCallId
from typing_extensions import Annotated
from langgraph.types import Command
from .models import BlueskyPost
from .converters import convert_post
from .utils import create_client, dump_debug_file
import logging

logger = logging.getLogger(__name__)


def get_posts_by_uris(
    tool_call_id: Annotated[str, InjectedToolCallId],
    uris: List[str],
    auth_handle: Optional[str] = None,
    auth_password: Optional[str] = None,
    debug: bool = True,
):
# ) -> Command:
    """Get post views for a specified list of posts by their AT-URIs.

    Args:
        tool_call_id (str): Unique identifier for this tool call, automatically injected by the framework
        uris (List[str]): List of post AT-URIs to fetch (e.g. ['at://did:plc:xyz/app.bsky.feed.post/tid'])
        auth_handle (Optional[str]): Handle for authentication if accessing private content
        auth_password (Optional[str]): Password for authentication if accessing private content
        debug (bool): If True, dumps raw post data to a debug file for troubleshooting

    Returns:
        Command: A Command object containing:
            - posts (Dict[str, BlueskyPost]): Posts keyed by their URI
            - messages (List[ToolMessage]): Status messages about the operation
    """
    client = create_client(auth_handle, auth_password)
    posts_dict: Dict[str, BlueskyPost] = {}
    raw_responses = []

    try:
        # The API has a limit on how many URIs can be fetched at once
        batch_size = 25
        for i in range(0, len(uris), batch_size):
            batch_uris = uris[i : i + batch_size]
            print("batch_uris", batch_uris)
            response = client.get_posts(uris=batch_uris)

            if debug:
                raw_responses.append(response.model_dump())

            for post in response.posts:
                posts_dict[post.uri] = convert_post(post)

        return Command(
            update={
                "posts": posts_dict,
                "messages": [
                    ToolMessage(
                        f"Successfully fetched {len(posts_dict)} posts",
                        tool_call_id=tool_call_id,
                    )
                ],
            }
        )

    except Exception as e:
        error = e
        logger.error(f"Error fetching posts: {str(e)}")
        raise

    finally:
        if debug:
            dump_debug_file(
                data=None,
                prefix="bluesky_get_posts",
                identifier=f"batch_{len(uris)}",
                raw_responses=raw_responses,
                processed_data={"posts": posts_dict} if posts_dict else None,
            )
