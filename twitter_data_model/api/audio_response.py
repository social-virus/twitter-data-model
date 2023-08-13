from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
    Field,
)


from .audio_space import AudioSpace
from .audio_space_search import AudioSpaceSearch


# pylint: disable=too-few-public-methods


class AudioSpaceResult(BaseModel):
    """Audio Space result class object."""

    audio_space: AudioSpace = Field(alias="audioSpace")


class AudioSpaceSearchResult(BaseModel):
    """Audio Space Search result class object."""

    search_by_raw_query: AudioSpaceSearch
