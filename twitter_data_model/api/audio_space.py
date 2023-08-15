from __future__ import annotations

from typing import (
    Dict,
    List,
    Literal,
    Optional,
)

from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
    Field,
)


from .tweet_response import TweetResult
from .user_response import User, UserResult


__all__ = [
    "AudioSpace",
]


# pylint: disable=too-few-public-methods


class AudioSpace(BaseModel):
    """Audio Space class object."""

    metadata: AudioSpaceMetadata
    sharings: AudioSpaceSharings
    participants: AudioSpaceParticipants


class AudioSpaceMetadata(BaseModel):
    """Audio Space Metadata class object."""

    rest_id: str
    media_key: str
    title: str
    state: str

    disallow_join: bool
    narrow_cast_space_type: int
    is_employee_only: bool
    is_locked: bool
    is_space_available_for_replay: bool
    is_space_available_for_clipping: bool
    conversation_controls: int
    total_replay_watched: int
    total_live_listeners: int

    creator_results: CreatorResults

    created_at: int
    updated_at: int
    scheduled_start: int
    started_at: int
    replay_start_time: int


class CreatorResults(BaseModel):
    """Creator Results class object."""

    result: User


class AudioSpaceSharings(BaseModel):
    """Audio Space Sharings class object."""

    items: List[AudioSpaceShare]
    slice_info: Dict  # TODO: resolve this?


class AudioSpaceShare(BaseModel):
    """Audio Space Share class object."""

    sharing_id: int
    created_at_ms: int
    updated_at_ms: int
    user_results: UserResult
    shared_item: AudioSpaceSharedTweet


class AudioSpaceSharedTweet(BaseModel):
    """Audio Space Shared Tweet class object."""

    typename: Literal["AudioSpaceSharedTweet"] = Field(alias="__typename")
    tweet_results: TweetResult


class AudioSpaceParticipants(BaseModel):
    """Audio Space Participants class object."""

    total: int
    admins: List[PeriscopeParticipant]
    speakers: List[PeriscopeParticipant]
    listeners: List[PeriscopeParticipant]


class PeriscopeParticipant(BaseModel):
    """Periscope Participant class object."""

    periscope_user_id: str
    start: Optional[int]
    twitter_screen_name: str
    display_name: str
    avatar_url: str

    is_verified: bool
    is_muted_by_admin: bool

    user_results: PeriscopeUserResult


class PeriscopeUserResult(BaseModel):
    """Periscope User Result class object."""

    rest_id: int
    result: PeriscopeUser


class PeriscopeUser(BaseModel):
    """Periscope User class object."""

    typename: Literal["User"] = Field(alias="__typename")
    identity_profile_labels_highlighted_label: IdentityProfileLabelsHighlightedLabel
    has_nft_avatar: bool
    is_blue_verified: bool
    legacy: Dict  # TODO: resolve this?


class IdentityProfileLabelsHighlightedLabel(BaseModel):
    """Identity Profile Labels Highlighted Label class object."""

    label: Optional[HighlightedLabel]


class HighlightedLabel(BaseModel):
    """Highlighted Label class object."""

    url: HighlightedLabelURL
    badge: HighlightedLabelURL
    description: str
    user_label_type: str = Field(alias="userLabelType")
    user_label_display_type: str = Field(alias="userLabelDisplayType")


class HighlightedLabelURL(BaseModel):
    """Highlighted Label URL class object."""

    url: str
    url_type: Optional[str] = Field(alias="urlType")


AudioSpace.update_forward_refs()
AudioSpaceMetadata.update_forward_refs()
AudioSpaceSharings.update_forward_refs()
AudioSpaceShare.update_forward_refs()
AudioSpaceSharedTweet.update_forward_refs()
AudioSpaceParticipants.update_forward_refs()
PeriscopeParticipant.update_forward_refs()
PeriscopeUserResult.update_forward_refs()
PeriscopeUser.update_forward_refs()

IdentityProfileLabelsHighlightedLabel.update_forward_refs()
HighlightedLabel.update_forward_refs()
HighlightedLabelURL.update_forward_refs()
