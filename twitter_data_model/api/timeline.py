from __future__ import annotations

from typing import (
    Annotated,
    Literal,
    List,
    Union,
)

from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
    Field,
)

# pylint: disable=relative-beyond-top-level

from .tweet_response import TweetResult
from .user_response import UserResult
from .utils import load_json


class TimelineEntry(BaseModel):
    """Timeline Entry class object."""

    entry_id: str = Field("entryId")
    sort_index: str = Field(alias="sortIndex")
    content: Union[TimelineTimelineItem, TimelineTimelineModule]

    @property
    def result(self):
        item = self.content.item_content
        if hasattr(item, "tweet_results"):
            return item.tweet_results.result

        if hasattr(item, "user_results"):
            return item.user_results.result

        raise AttributeError(
            "Invalid Timeline Entry: missing 'tweet_results' or 'user_results'."
        )

    @classmethod
    def from_json(cls, pathname: str):
        """Load class object from JSON file."""
        data = load_json(pathname)
        return cls(**data)


TimelineItemType = Annotated[
    Union["TimelineTweet", "TimelineUser"], Field(discriminator="typename")
]


class TimelineTimelineItem(BaseModel):
    """Timeline Timeline Item class object."""

    typename: Literal["TimelineTimelineItem"] = Field(alias="__typename")
    entry_type: Literal["TimelineTimelineItem"] = Field(alias="entryType")
    item_content: TimelineItemType = Field(alias="itemContent")


class TimelineTimelineModule(BaseModel):
    typename: Literal["TimelineTimelineModule"] = Field(alias="__typename")
    entry_type: Literal["TimelineTimelineModule"] = Field(alias="entryType")
    items: List[HomeConversation]

    # TODO: test and validate this.
    def __iter__(self):
        for item in self.items:
            yield item.item.item_content


class HomeConversation(BaseModel):
    """Home Conversation class object."""

    entry_id: str = Field(alias="entryId")
    dispensable: bool
    item: TimelineItemContent


class TimelineItemContent(BaseModel):
    """Timeline Item Content class object."""

    item_content: TimelineTweet = Field(alias="itemContent")


class TimelineTweet(BaseModel):
    """Timeline Tweet class object."""

    typename: Literal["TimelineTweet"] = Field(alias="__typename")
    item_type: Literal["TimelineTweet"] = Field(alias="itemType")
    tweet_results: TweetResult


class TimelineUser(BaseModel):
    """Timeline User class object."""

    typename: Literal["TimelineUser"] = Field(alias="__typename")
    item_type: Literal["TimelineUser"] = Field(alias="itemType")
    user_results: UserResult


TimelineEntry.update_forward_refs()
TimelineTimelineItem.update_forward_refs()
TimelineTimelineModule.update_forward_refs()
HomeConversation.update_forward_refs()
TimelineItemContent.update_forward_refs()
