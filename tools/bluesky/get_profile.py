"""AI Agent tool wrapper to fetch Bluesky profile w/ Bluesky API"""

import json
from datetime import datetime
from pathlib import Path
import logging
from typing_extensions import Optional
from .converters import convert_profile
from .utils import create_client
from langgraph.types import Command
from langchain_core.messages import ToolMessage
from langchain_core.tools.base import InjectedToolCallId
from typing_extensions import Annotated

logger = logging.getLogger(__name__)


def get_profile(
    tool_call_id: Annotated[str, InjectedToolCallId],
    handle: str,
    auth_handle: Optional[str] = None,
    auth_password: Optional[str] = None,
    debug: bool = False,
):
    # ) -> Command:
    """
    Get detailed profile information for a Bluesky user.

    Args:
        tool_call_id: Unique identifier for this tool call, automatically injected by the framework
        handle: The user's handle (e.g. 'example.bsky.social')
        auth_handle: Optional handle for authentication. If None, uses env vars
        auth_password: Optional password for authentication. If None, uses env vars
        debug: If True, dumps raw profile data to a debug file

    Returns:
        Command containing the profile information and success message
    """
    client = create_client(auth_handle, auth_password)

    try:
        profile_response = client.get_profile(actor=handle)

        if debug:
            debug_path = Path("debug")
            debug_path.mkdir(exist_ok=True)
            with open(
                debug_path
                / f'bluesky_profile_{handle}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json',
                "w",
            ) as f:
                json.dump(profile_response.model_dump(), f, indent=2, default=str)

        profile = convert_profile(profile_response)
        return {
            "bluesky_profile": profile,
        }
        # return Command(
        #     update={
        #         "bluesky_profile": profile,
        #         "messages": [
        #             ToolMessage(
        #                 "Successfully fetched profile", tool_call_id=tool_call_id
        #             )
        #         ],
        #     }
        # )

    except Exception as e:
        logger.error(f"Error fetching profile for {handle}: {str(e)}")
        raise
