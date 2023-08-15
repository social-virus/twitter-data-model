"""
Global API response class objects.
"""

from __future__ import annotations

from typing import (
    Dict,
    List,
    Union,
)


from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
)

# pylint: disable=relative-beyond-top-level

from .audio_response import (
    AudioSpaceResult,
    AudioSpaceSearchResult,
)

from .tweet_response import (
    Tweet,
    TweetResultAlt,
    TweetStatsResponse,
)

from .user_response import (
    User,
    UserResponse,
    UserResult,
    UsersResult,
)

from .utils import load_json


__all__ = [
    "DataResponseList",
    "DataResponse",
    "DataResult",
]


class DataResponseList(BaseModel):
    """Collect a list of Data Response objects."""

    __root__: List[DataResponse]
    
    def __delitem__(self, item: int) -> None:
        del self.__root__[item]
    
    def __getitem__(self, item: int) -> DataResponse:
        return self.__root__[item]
    
    def __iter__(self):
        for item in self.__root__:
            yield item
    
    def __len__(self):
        return len(self.__root__)

    @classmethod
    def from_json(cls, pathname: str):
        """Load class object from JSON file."""
        data = load_json(pathname)
        return cls.parse_obj(data)


class DataResponse(BaseModel):
    """Data Response class object."""

    data: Union[
        DataResult,
        TweetResultAlt,
        UserResponse,
        UserResult,
        UsersResult,
        AudioSpaceResult,
        AudioSpaceSearchResult,
    ]

    def resolve(self):
        if isinstance(self.data, (DataResult, TweetResultAlt, UserResponse)):
            return self.data.resolve()

        if isinstance(self.data, UsersResult):
            return self.data.users  # resolve()

        if isinstance(self.data, AudioSpaceResult):
            return self.data.audio_space

        if isinstance(self.data, AudioSpaceSearchResult):
            return self.data.search_by_raw_query

        return self.data

    @classmethod
    def from_json(cls, pathname: str):
        """Load class object from JSON file."""
        data = load_json(pathname)
        return cls(**data)


class DataResult(BaseModel):
    """Data Result class object."""

    result: Union[
        User,
        UserResponse,
        Tweet,
        TweetStatsResponse,
    ]

    def resolve(self):
        if isinstance(self.result, (User, Tweet)):
            return self.result

        if isinstance(self.result, UserResponse):
            return self.resolve()

        if isinstance(self.result, TweetStatsResponse):
            return self.result.user.tweet_stats

        return self.result

    @classmethod
    def from_json(cls, pathname: str) -> Dict:
        """Load class object from JSON file."""
        data = load_json(pathname)
        return cls(**data)


DataResponseList.update_forward_refs()
DataResponse.update_forward_refs()
DataResult.update_forward_refs()
