"""Twitter User object class."""

from __future__ import annotations

import json

from pathlib import Path
from typing import (
    Annotated,
    Dict,
    Literal,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
)


from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
    Field,
)


from .common import BaseMixin
from .user_verify import VerificationInfo


__all__ = [
    "User",
    "UserUnavailable",
    "UserType",
]


# pylint: disable=too-few-public-methods


class UserUnavailable(BaseModel):
    """For instances of users whom are unavailable."""

    typename: Literal["UserUnavailable"] = Field(alias="__typename")
    reason: str


class Birthdate(BaseModel):
    """Affiliates Highlighted Label Birthdate object."""

    day: int
    month: int
    visibility: str
    year_visibility: str


class AffiliatesHighlightedLabel(BaseModel):
    """Affiliates Highlighted Label object."""

    birthdate: Optional[Birthdate]


class User(BaseModel, BaseMixin):
    """User object."""

    typename: Literal["User"] = Field(alias="__typename")
    id: str
    rest_id: int
    affiliates_highlighted_label: AffiliatesHighlightedLabel
    has_graduated_access: Optional[bool]
    is_blue_verified: bool
    profile_image_shape: Optional[str] = Field(alias="profileImageShape")
    legacy: UserLegacy
    is_profile_translatable: Optional[bool]
    smart_blocked_by: Optional[bool]
    smart_blocking: Optional[bool]
    legacy_extended_profile: Optional[AffiliatesHighlightedLabel]
    verification_info: Optional[VerificationInfo]
    business_account: Optional[BusinessAccount]
    professional: Optional[Professional]

    def __contains__(self, item: str):
        if isinstance(item, int):
            return item == self.rest_id

        return item.casefold() in [
            self.id.casefold(),
            self.legacy.name.casefold(),
            self.legacy.screen_name.casefold(),
        ]

    def __getattr__(self, key):
        try:
            return self.__dict__[key]
        except KeyError as error:
            if hasattr(self.legacy, key):
                return getattr(self.legacy, key)
            raise KeyError from error


class UserLegacy(BaseModel):
    """User Legacy object."""

    blocked_by: Optional[bool]
    can_dm: Optional[bool]
    can_media_tag: Optional[bool]
    created_at: str
    default_profile: bool
    default_profile_image: bool
    description: str
    entities: UserEntities
    fast_followers_count: int
    favorites_count: int = Field(alias="favourites_count")
    followers_count: int
    friends_count: int
    has_custom_timelines: bool
    is_translator: bool
    listed_count: int
    location: str
    media_count: int
    name: str
    normal_followers_count: int
    pinned_tweet_ids_str: List[str]
    possibly_sensitive: bool
    profile_image_url: Optional[str]
    profile_image_url_https: Optional[str]
    profile_banner_url: Optional[str]
    profile_interstitial_type: str
    screen_name: str
    statuses_count: int
    translator_type: str
    url: Optional[str]
    verified: bool
    want_retweets: Optional[bool]
    withheld_in_countries: List[str]
    withheld_scope: Optional[str]


class UserEntities(BaseModel):
    """User Entities object."""

    description: UserEntitiesDescription
    url: Optional[UserEntitiesURLs]


class UserEntitiesDescription(BaseModel):
    """User Entities Description object."""

    urls: List[UserEntitiesURL]


class UserEntitiesURLs(BaseModel):
    """User Entities URLs (plural) object."""

    urls: List[UserEntitiesURL]


class UserEntitiesURL(BaseModel):
    """User Entities URL (singular) object."""

    display_url: str
    expanded_url: str
    url: str
    indices: Tuple[int, int]


class BusinessAccount(BaseModel):
    """Business Account object."""

    # TODO: resolve definition
    pass  # pylint: disable=unnecessary-pass


class Professional(BaseModel):
    """Professional object."""

    rest_id: str
    professional_type: str
    category: List[ProfessionalCategory]


class ProfessionalCategory(BaseModel):
    """Professional Category object."""

    id: int
    name: str
    icon_name: str


UserType = Annotated[Union[User, UserUnavailable], Field(discriminator="typename")]


class UserList(BaseModel):
    """User List class object."""

    __root__: List[UserType]

    def __contains__(self, item: Union[int, str]) -> bool:
        if isinstance(item, str):
            names = []

            for entry in self:
                if isinstance(entry, Dict):
                    if entry["typename"] == "User":
                        entry = User(**entry)
                    elif entry["typename"] == "UserUnavailable":
                        entry = UserUnavailable(**entry)
                    else:
                        continue

                names += [
                    entry.legacy.name.casefold(),
                    entry.legacy.screen_name.casefold(),
                    entry.id,
                ]

            return item in names

        if isinstance(item, int):
            rest_ids = [entry.rest_id for entry in self if isinstance(entry, User)]

            return item in rest_ids

        return False

    def __delattr__(self, attr: Union[int, str]) -> None:
        for index, entry in enumerate(self.__root__):
            if attr in entry:
                del self.__root__[index]

    def __iter__(self):
        for entry in self.__root__:
            yield entry

    def __len__(self):
        return len(self.__root__)

    __delitem__ = __delattr__

    def get_rest_ids(self) -> List[int]:
        """Return a list of Rest IDs."""

        return [user.rest_id for user in self]

    @classmethod
    def from_json(cls, pathname: str) -> Dict:
        """Convert file data to class object."""

        data = Path(pathname).read_text(encoding="utf8")
        return cls.parse_obj(json.loads(data))

    @classmethod
    def parse_obj(cls, data):
        """Flatten a full DataResponse JSON."""

        results = []

        if isinstance(data, str):
            data = json.loads(data)

        for datum in data:
            if isinstance(datum, str):
                continue

            if "data" in datum and "user" in datum["data"].keys():
                result = datum["data"]["user"]["result"]
                results.append(result)
            else:
                # TODO: What form should this data take?
                # TODO: What error(s) should this raise?
                results.append(datum)

        return super().parse_obj(results)


User.update_forward_refs()
UserLegacy.update_forward_refs()
UserEntities.update_forward_refs()
UserEntitiesDescription.update_forward_refs()
UserEntitiesURLs.update_forward_refs()
Professional.update_forward_refs()
