from __future__ import annotations


from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
    Field,
)


from .tweet import Tweet


# pylint: disable=too-few-public-methods


class TweetResultAlt(BaseModel):
    """Tweet Result (alternate) class object."""

    tweet_result: TweetResult = Field(alias="tweetResult")

    def resolve(self):
        return self.tweet_result.result


class TweetResult(BaseModel):
    """Tweet Result class object."""

    result: Tweet


class TweetStatsResponse(BaseModel):
    """Tweet Stats response class object."""

    user: TweetStatsResult


class TweetStatsResult(BaseModel):
    """Tweet Stats result class object."""

    tweet_stats: TweetStats


class TweetStats(BaseModel):
    """Tweet Stats class object."""

    tweet_frequency: int


TweetResultAlt.update_forward_refs()
TweetStatsResponse.update_forward_refs()
TweetStatsResult.update_forward_refs()
