from __future__ import annotations

from typing import (
    List,
    Optional,
)

from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
)


from .user_response import UserResult


__all__ = [
    "Card",
]


# pylint: disable=too-few-public-methods


class Card(BaseModel):
    """Card object."""

    rest_id: str
    legacy: CardLegacy


class CardLegacy(BaseModel):
    """Card Legacy object."""

    binding_values: List[BindingValues]
    card_platform: CardPlatform
    name: str
    url: str
    user_refs_results: Optional[List[UserResult]]


class CardPlatformValue(BaseModel):
    """Card Platform Value object."""

    name: str
    version: Optional[str]


class CardPlatformPlatform(BaseModel):
    """Card Platform Platform object."""

    audience: CardPlatformValue
    device: CardPlatformValue


class CardPlatform(BaseModel):
    """Card Platform object."""

    platform: CardPlatformPlatform


class BindingValue(BaseModel):
    """Binding Value object."""

    scribe_key: Optional[str]
    user_value: Optional[UserValue]
    image_value: Optional[ImageValue]
    string_value: Optional[str]
    type: str


class BindingValues(BaseModel):
    """Binding Values object."""

    key: str
    value: BindingValue


class ImageValue(BaseModel):
    """Image Value object."""

    height: int
    width: int
    url: str


class UserValue(BaseModel):
    """User Value object."""

    id_str: str
    path: List[str]


class ThumbnailImageColor(BaseModel):
    """Thumbnail Image Color object."""

    image_color_value: ImageColorValue


class ImageColorValue(BaseModel):
    """Image Color Value object."""

    palette: List[ImagePalette]


class ImagePalette(BaseModel):
    """Image Palette object."""

    rgb: RGBSpec


class RGBSpec(BaseModel):
    """RGB specification."""

    red: int
    green: int
    blue: int
    percentage: float


class UnifiedCard(BaseModel):
    """Unified Card object."""

    card_fetch_state: str


Card.update_forward_refs()
CardLegacy.update_forward_refs()
BindingValue.update_forward_refs()
