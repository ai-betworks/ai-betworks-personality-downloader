"""Converts Bluesky data from AT Protocol to our data models

Effectively, this is used to compress the AT Protocol data to save on tokens + avoid hitting context limits when we analyze the Bluesky data"""

from typing import Any, Optional, List, Union, cast
from .models import (
    BlueskyProfile,
    BlueskyPost,
    ImageEmbed,
    VideoEmbed,
    ExternalEmbed,
    RecordEmbed,
    RecordWithMediaEmbed,
    AspectRatio,
)


def convert_profile(profile_view: Any) -> BlueskyProfile:
    """Convert AT Protocol profile view to BlueskyProfile"""
    # Handle blocked authors
    if getattr(profile_view, "py_type", None) == "app.bsky.feed.defs#blockedAuthor":
        return BlueskyProfile(
            did=profile_view.did,
            handle="blocked_user",  # Use placeholder since handle isn't available
            display_name=None,
            description=None,
            avatar_url=None,
            followers_count=0,
            follows_count=0,
            posts_count=0,
            indexed_at=None,
            blocked=True,
        )

    # Regular profile conversion
    return BlueskyProfile(
        did=profile_view.did,
        handle=profile_view.handle,
        display_name=getattr(profile_view, "displayName", None),
        description=getattr(profile_view, "description", None),
        avatar_url=getattr(profile_view, "avatar", None),
        followers_count=getattr(profile_view, "followersCount", 0),
        follows_count=getattr(profile_view, "followsCount", 0),
        posts_count=getattr(profile_view, "postsCount", 0),
        indexed_at=getattr(profile_view, "indexedAt", None),
    )


def convert_embed(
    embed_view: Any,
) -> Optional[
    Union[
        List[ImageEmbed],
        ImageEmbed,
        VideoEmbed,
        ExternalEmbed,
        RecordEmbed,
        RecordWithMediaEmbed,
    ]
]:
    """Convert AT Protocol embed view to our embed types"""
    if not embed_view:
        return None

    if embed_view.py_type == "app.bsky.embed.images#view":
        # Multiple images
        if len(embed_view.images) > 1:
            return [
                ImageEmbed(
                    alt=getattr(img, "alt", None),
                    fullsize=img.fullsize,
                    thumb=img.thumb,
                    aspect_ratio=(
                        AspectRatio(
                            width=img.aspect_ratio.width,
                            height=img.aspect_ratio.height,
                        )
                        if hasattr(img, "aspect_ratio") and img.aspect_ratio is not None
                        else None
                    ),
                )
                for img in embed_view.images
            ]
        # Single image
        img = embed_view.images[0]
        embed: ImageEmbed = {
            "alt": getattr(img, "alt", None),
            "fullsize": img.fullsize,
            "thumb": img.thumb,
        }
        if hasattr(img, "aspect_ratio") and img.aspect_ratio is not None:
            embed["aspect_ratio"] = AspectRatio(
                width=img.aspect_ratio.width,
                height=img.aspect_ratio.height,
            )
        return embed

    elif embed_view.py_type == "app.bsky.embed.video#view":
        embed: VideoEmbed = {
            "alt": getattr(embed_view, "alt", None),
            "thumbnail": embed_view.thumbnail,
            "playlist": embed_view.playlist,
        }
        if hasattr(embed_view, "aspect_ratio") and embed_view.aspect_ratio is not None:
            embed["aspect_ratio"] = AspectRatio(
                width=embed_view.aspect_ratio.width,
                height=embed_view.aspect_ratio.height,
            )
        return embed

    elif embed_view.py_type == "app.bsky.embed.external#view":
        return ExternalEmbed(
            uri=embed_view.external.uri,
            title=embed_view.external.title,
            description=embed_view.external.description,
            thumb=getattr(embed_view.external, "thumb", None),
        )

    elif embed_view.py_type == "app.bsky.embed.record#view":
        record = embed_view.record
        # Handle not found records
        if getattr(record, "py_type", None) == "app.bsky.embed.record#viewNotFound":
            embed = RecordEmbed(
                uri=record.uri,
                not_found=True,
                author=None,
                value=None,
                labels=[],
            )
            return embed

        # Handle blocked records
        if getattr(record, "py_type", None) == "app.bsky.embed.record#viewBlocked":
            embed = RecordEmbed(
                uri=record.uri,
                blocked=True,
                author=(
                    convert_profile(record.author)
                    if hasattr(record, "author")
                    else None
                ),
                value=None,
                labels=[],
            )
            return embed

        # Handle StarterPackViewBasic which has different field names
        if (
            getattr(record, "py_type", None)
            == "app.bsky.graph.defs#starterPackViewBasic"
        ):
            embed = RecordEmbed(
                uri=record.uri,
                cid=record.cid,
                author=(
                    convert_profile(record.creator)
                    if hasattr(record, "creator")
                    else None
                ),
                value=(
                    record.record.model_dump()
                    if hasattr(record.record, "model_dump")
                    else record.record
                ),
                labels=getattr(record, "labels", []),
            )
            return embed

        # Handle GeneratorView type
        if getattr(record, "py_type", None) == "app.bsky.feed.defs#generatorView":
            embed = RecordEmbed(
                uri=record.uri,
                cid=getattr(record, "cid", None),
                author=(
                    convert_profile(record.creator)
                    if hasattr(record, "creator")
                    else None
                ),
                value={
                    "did": getattr(record, "did", None),
                    "display_name": getattr(record, "display_name", None),
                    "description": getattr(record, "description", None),
                    "avatar": getattr(record, "avatar", None),
                    "like_count": getattr(record, "like_count", 0),
                },
                labels=getattr(record, "labels", []),
            )
            return embed

        # Handle ListView type
        if getattr(record, "py_type", None) == "app.bsky.graph.defs#listView":
            embed = RecordEmbed(
                uri=record.uri,
                cid=getattr(record, "cid", None),
                author=(
                    convert_profile(record.creator)
                    if hasattr(record, "creator")
                    else None
                ),
                value={
                    "name": getattr(record, "name", None),
                    "purpose": getattr(record, "purpose", None),
                    "description": getattr(record, "description", None),
                    "avatar": getattr(record, "avatar", None),
                    "list_item_count": getattr(record, "list_item_count", 0),
                },
                labels=getattr(record, "labels", []),
            )
            return embed

        # Regular record embed
        embed = RecordEmbed(
            uri=record.uri,
            cid=getattr(record, "cid", None),
        )

        # For feed posts, only include minimal data
        if getattr(record.value, "py_type", None) == "app.bsky.feed.post":
            # embed["author_did"] = record.author.did
            embed["author_handle"] = record.author.handle
            embed["text"] = record.value.text
        else:
            # For other record types, include full value
            embed["value"] = (
                record.value.model_dump()
                if hasattr(record.value, "model_dump")
                else record.value
            )

        # Only include labels if they exist and are not empty
        if hasattr(record, "labels") and record.labels:
            embed["labels"] = record.labels

        # Only include embeds if they exist and are not empty
        if hasattr(record, "embeds") and record.embeds:
            converted_embeds = [
                e for e in (convert_embed(e) for e in record.embeds) if e is not None
            ]
            if converted_embeds:
                embed["embeds"] = converted_embeds

        return embed

    elif embed_view.py_type == "app.bsky.embed.recordWithMedia#view":
        return RecordWithMediaEmbed(
            record=convert_embed(embed_view.record),  # type: ignore
            media=convert_embed(embed_view.media),  # type: ignore
        )

    return None


def convert_post(post_view: Any) -> BlueskyPost:
    """Convert AT Protocol post view to BlueskyPost"""
    record = post_view.record

    post = BlueskyPost(
        uri=post_view.uri,
        # cid=post_view.cid,
        # author_did=post_view.author.did,
        author_handle=post_view.author.handle,
        text=record.text,
        # created_at=record.created_at,
        # indexed_at=post_view.indexed_at,
        reply_count=getattr(post_view, "reply_count", 0),
        repost_count=getattr(post_view, "repost_count", 0),
        like_count=getattr(post_view, "like_count", 0),
        quote_count=getattr(post_view, "quote_count", 0),
    )

    # Add reply references if this is a reply
    reply = getattr(post_view, "reply", None)
    if reply is not None:
        if hasattr(reply, "parent"):
            post["reply_to_parent"] = reply.parent.uri
        if hasattr(reply, "root"):
            post["reply_to_root"] = reply.root.uri

    # Add embed if present
    embed = convert_embed(getattr(post_view, "embed", None))
    if embed is not None:
        post["embed"] = embed

    return post
