"""Media class definitions."""

from __future__ import annotations

from typing import (
    List,
    Optional,
    Tuple,
)


from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
    Field,
)


from .user_response import UserResult


# pylint: disable=too-few-public-methods


class EntityURL(BaseModel):
    """Entity URL"""

    display_url: str
    expanded_url: str
    url: str
    indices: Tuple[int, int]


class ExtendedMediaAvailability(BaseModel):
    """Extended Media Availability"""

    status: str


class Hashtag(BaseModel):
    """Hashtag"""

    indices: Tuple[int, int]
    text: str


class MediaFaces(BaseModel):
    """Media Faces"""

    faces: List[FocusRects]


class MediaFeatures(BaseModel):
    """Media Features"""

    large: Optional[MediaFaces]
    medium: Optional[MediaFaces]
    small: Optional[MediaFaces]
    orig: Optional[MediaFaces]


class AdditionalMediaInfo(BaseModel):
    """Additional Media Info"""

    monetizeable: Optional[bool]
    source_user: Optional[UserResult]


class Media(BaseModel):
    """Media"""

    display_url: str
    expanded_url: str
    id_str: str
    indices: Tuple[int, int]
    media_key: Optional[str]
    media_url_https: str
    type: str  # animated_gif
    url: str
    ext_media_availability: Optional[ExtendedMediaAvailability]
    features: Optional[MediaFeatures]
    sizes: ImageSizes
    original_info: OriginalInfo
    video_info: Optional[VideoInfo]
    additional_media_info: Optional[AdditionalMediaInfo]
    media_stats: Optional[MediaStats] = Field(alias="mediaStats")


class MediaStats(BaseModel):
    """Media Stats class object."""

    view_count: int = Field(alias="viewCount")


class Symbol(BaseModel):
    """Symbol"""

    pass


class ImageSize(BaseModel):
    """Image Size"""

    h: int
    w: int
    resize: str


class ImageSizes(BaseModel):
    """Image Size list container"""

    large: ImageSize
    medium: ImageSize
    small: ImageSize
    thumb: ImageSize


class FocusRects(BaseModel):
    """Focus Rects corner points."""

    x: int
    y: int
    w: int
    h: int


class OriginalInfo(BaseModel):
    """Original Info"""

    height: int
    width: int
    focus_rects: Optional[List[FocusRects]]


class VideoInfo(BaseModel):
    """Video Info"""

    aspect_ratio: List[int]
    duration_millis: Optional[int]
    variants: List[VideoVariant]


class VideoVariant(BaseModel):
    """Video Variant"""

    bitrate: Optional[int]
    content_type: str
    url: str


Media.update_forward_refs()
MediaFaces.update_forward_refs()
VideoInfo.update_forward_refs()
