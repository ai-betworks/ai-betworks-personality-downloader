"""Utilities for Bluesky API including authentication and debug helpers"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Optional, List, Dict
from atproto import Client
from dotenv import load_dotenv

load_dotenv()


def create_client(
    handle: Optional[str] = None, password: Optional[str] = None
) -> Client:
    """
    Create an authenticated Bluesky client.

    Args:
        handle: Bluesky handle (e.g. 'user.bsky.social'). If None, uses BLUESKY_HANDLE env var
        password: Account password or app password. If None, uses BLUESKY_PASSWORD env var

    Returns:
        Authenticated Client instance

    Raises:
        ValueError: If credentials are not provided and not found in environment
        Exception: If authentication fails
    """
    # Get credentials from args or environment
    handle = handle or os.getenv("BLUESKY_HANDLE")
    password = password or os.getenv("BLUESKY_PASSWORD")

    if not handle or not password:
        raise ValueError(
            "Bluesky credentials not found. Either provide them as arguments or "
            "set BLUESKY_HANDLE and BLUESKY_PASSWORD environment variables."
        )

    # Create and authenticate client
    client = Client()
    client.login(handle, password)

    return client


def dump_debug_file(
    data: Any,
    prefix: str,
    identifier: str = "",
    raw_responses: list[Any] | None = None,
    processed_data: Any | None = None,
) -> None:
    """Dumps debug data to a file with consistent naming and structure.

    Args:
        data: The data to dump if no raw_responses/processed_data provided
        prefix: Prefix for the debug file name (e.g. 'bluesky_posts')
        identifier: Optional identifier to include in filename (e.g. user handle)
        raw_responses: Optional list of raw API responses
        processed_data: Optional processed/converted data
    """
    debug_path = Path("debug")
    debug_path.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = (
        f"{prefix}_{identifier}_{timestamp}.json"
        if identifier
        else f"{prefix}_{timestamp}.json"
    )

    if raw_responses is not None or processed_data is not None:
        output = {"raw": raw_responses or [], **processed_data}
    else:
        output = data

    with open(debug_path / filename.replace("@", ""), "w") as f:
        json.dump(output, f, indent=2, default=str)


def reduce_bluesky_posts(bluesky_posts: List[Dict[str, Any]]) -> List[str]:
    """
    Reduces a list of Bluesky posts to just their text content.

    Args:
        bluesky_posts: List of Bluesky post objects

    Returns:
        List of post text strings
    """
    return [post["text"] for post in bluesky_posts]


def reduce_bluesky_replies(
    bluesky_replies: List[Dict[str, Any]]
) -> List[List[Dict[str, str]]]:
    """
    Reduces a list of Bluesky reply threads to simplified format containing just text and author handles.

    Args:
        bluesky_replies: List of Bluesky reply thread objects

    Returns:
        List of reply threads, where each thread is a list of dicts containing text and speaker
    """
    reduced_replies = []
    for outer_reply in bluesky_replies:
        reply_thread = []
        for reply_in_thread in outer_reply.get("reply_context"):
            reply_thread.append(
                {
                    "text": reply_in_thread.get("text"),
                    "speaker": reply_in_thread.get("author_handle"),
                }
            )
        reply_thread.append(
            {
                "text": outer_reply.get("post").get("text"),
                "speaker": outer_reply.get("post").get("author_handle"),
            }
        )
        reduced_replies.append(reply_thread)
    return reduced_replies


def format_replies_as_xml(reduced_replies: List[List[Dict[str, str]]]) -> str:
    """
    Formats reduced Bluesky replies into an XML-like string format.

    Args:
        reduced_replies: List of reply threads from reduce_bluesky_replies

    Returns:
        String in XML-like format containing the replies
    """
    output = ["<replies>"]

    for reply_thread in reduced_replies:
        output.append("  <reply>")
        for message in reply_thread:
            output.append("    <message>")
            output.append(f"      <speaker>{message['speaker']}</speaker>")
            output.append(f"      <text>{message['text']}</text>")
            output.append("    </message>")
        output.append("  </reply>")

    output.append("</replies>")
    return "\n".join(output)
