from __future__ import annotations

from typing import (
    List,
    Union,
)


from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
)


from .user import User


# pylint: disable=too-few-public-methods


class UserResponse(BaseModel):
    """User Response class object."""

    user: Union[
        User,
        UserResult,
    ]

    def resolve(self):
        if isinstance(self.user, UserResult):
            return self.user.result
        return self.user


class UserResult(BaseModel):
    """User Result class object."""

    result: User


class UserResults(BaseModel):
    """User Results class object."""

    user_results: UserResult

    def resolve(self):
        return self.user_results.result


class UsersResult(BaseModel):
    """Users Result class object."""

    users: List[UserResult]

    def __iter__(self):
        for item in self.users:
            yield item

    def resolve(self):
        return self.users


UserResponse.update_forward_refs()
UserResult.update_forward_refs()
