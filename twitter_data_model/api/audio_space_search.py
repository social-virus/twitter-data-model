from __future__ import annotations

from typing import (
    List,
    Literal,
)

from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
)


__all__ = [
    "AudioSpaceSearch",
]


# pylint: disable=too-few-public-methods


class AudioSpaceSearch(BaseModel):
    """Audio Space Search class object."""

    audio_spaces_grouped_by_section: AudioSpaceSections


class AudioSpaceSections(BaseModel):
    """Audio Space Sections class object."""

    sections: List[AudioSpaceSection]


class AudioSpaceSection(BaseModel):
    """Audio Space Section class object."""

    name: str
    items: List[AudioSpaceItem]
    destination: str


class AudioSpaceItem(BaseModel):
    """Audio Space item class object."""

    kind: Literal["Audiospace"]
    followed_participants_results: List  # TODO: resolve this
    space: AudioSpaceRestId


class AudioSpaceRestId(BaseModel):
    """Audio Space REST Id object."""

    rest_id: str


AudioSpaceSearch.update_forward_refs()
AudioSpaceSections.update_forward_refs()
AudioSpaceSection.update_forward_refs()
AudioSpaceItem.update_forward_refs()
AudioSpaceRestId.update_forward_refs()
