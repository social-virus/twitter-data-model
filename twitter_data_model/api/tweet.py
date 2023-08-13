"""Twitter Tweet object class definitions."""

from __future__ import annotations

from typing import (
    Dict,
    List,
    Literal,
    Optional,
    Tuple,
)

from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
    Field,
)


from .common import BaseMixin

from .card import (
    Card,
    UnifiedCard,
)
from .media import (
    EntityURL,
    Hashtag,
    Symbol,
    Media,
)

# from .timeline_user import UserResults
from .user_response import UserResults

# pylint: disable=too-few-public-methods

# TODO: validate this as correct.
# https://twitter.com/kepano/status/1684370892263145472
# TweetDoesNotExist (not same as TweetUnavailable?)
# [{'data': {'user': {}}}]
class TweetUnavailable(BaseModel):
    typename: str = Field(alias="__typename")
    reason: str


class Tweet(BaseModel, BaseMixin):
    """Tweet class object."""

    typename: Literal["Tweet"] = Field(alias="__typename")
    rest_id: int
    has_birdwatch_notes: Optional[bool]
    core: UserResults
    card: Optional[Card]
    unified_card: Optional[UnifiedCard]
    unmention_data: Optional[Dict]
    edit_control: TweetEditControl
    edit_perspective: Optional[TweetEditPerspective]
    is_translatable: bool
    views: TweetViews
    source: str
    legacy: TweetLegacy
    quick_promote_eligibility: Optional[QuickPromoteEligibility]

    @property
    def user(self):
        return self.core.user_results.result


class TweetEditControl(BaseModel):
    """Tweet Edit Control class object."""

    edit_tweet_ids: List[str]
    editable_until_msecs: int
    is_edit_eligible: bool
    edits_remaining: int


class TweetEditPerspective(BaseModel):
    """Tweet Edit Perspective class object."""

    favorited: bool
    retweeted: bool


class TweetViews(BaseModel):
    """Tweet Views class object."""

    state: str
    count: Optional[int]


class TweetLegacy(BaseModel):
    """Tweet Legacy class object."""

    created_at: str
    conversation_id_str: str
    bookmark_count: Optional[int]
    bookmarked: Optional[bool]
    display_text_range: List[int]
    entities: TweetEntities
    extended_entities: Optional[TweetEntities]
    favorite_count: int
    favorited: bool
    full_text: str
    in_reply_to_screen_name: Optional[str]
    in_reply_to_status_id_str: Optional[str]
    in_reply_to_user_id_str: Optional[str]
    is_quote_status: bool
    lang: str
    possibly_sensitive: Optional[bool]
    possibly_sensitive_editable: Optional[bool]
    quote_count: int
    reply_count: int
    retweet_count: int
    retweeted: bool
    user_id_str: str
    id_str: str
    self_thread: Optional[SelfThread]
    scopes: Optional[TweetScopes]


class TweetEntities(BaseModel):
    """Tweet Entities class object."""

    user_mentions: Optional[List[UserMention]]
    urls: Optional[List[EntityURL]]
    hashtags: Optional[List[Hashtag]]
    symbols: Optional[List[Symbol]]
    media: Optional[List[Media]]


class TweetScopes(BaseModel):
    """Tweet Scopes class object."""

    followers: bool


class UserMention(BaseModel):
    """User Mention class object."""

    id_str: str
    name: str
    screen_name: str
    indices: Tuple[int, int]


class QuickPromoteEligibility(BaseModel):
    """Quick Promote Eligibility class object."""

    eligibility: str


class SelfThread(BaseModel):
    """Tweet Self Thread class object."""

    id_str: str


Tweet.update_forward_refs()
TweetLegacy.update_forward_refs()
TweetEntities.update_forward_refs()
EntityURL.update_forward_refs()
