from unittest import (
    TestCase,
    main,
)

import context

from api.response import (
    DataResponse,
)


class TestAudioSpace(TestCase):
    def test_audio_space(self):
        data = DataResponse.from_json("data/AudioSpaceById.json")

    def test_audio_space_search(self):
        data = DataResponse.from_json("data/AudioSpaceSearch.json")


if __name__ == "__main__":
    main()
