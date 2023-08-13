from unittest import (
    TestCase,
    main,
)

import context

from api.response import (
    DataResponse,
    DataResult,
)

from api.timeline import (
    TimelineEntry,
)


class TestUsers(TestCase):
    def test_users_by_screen_name(self):
        data = DataResponse.from_json("data/UserByScreenName.json")

    def test_users_by_rest_ids(self):
        data = DataResponse.from_json("data/UsersByRestIds.json")

    def test_user_likes(self):
        data = TimelineEntry.from_json("data/Likes.json")

    def test_user_media(self):
        data = TimelineEntry.from_json("data/UserMedia.json")


    def test_user_followers(self):
        data = TimelineEntry.from_json("data/Followers.json")


    def test_user_following(self):
        data = TimelineEntry.from_json("data/Following.json")


"""
# TODO: resolve this looping issue
print("-" * 50)
data = load_json("data/UsersByRestIds.json")
data = DataResponse(**data)
for _, datum in data:
    for entry in datum:
        print(entry)
"""

if __name__ == "__main__":
    main()
