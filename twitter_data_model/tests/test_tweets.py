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


class TestTweets(TestCase):
    def test_tweet_stats(self):
        data = DataResponse.from_json("data/TweetStats.json")

    def test_tweets_by_rest_id(self):
        data = DataResponse.from_json("data/TweetResultsByRestId.json")

    def test_user_tweets(self):
        # Singular (non-list) response
        data = TimelineEntry.from_json("data/UserTweets.json")

    def test_user_tweets_and_replies(self):
        # Singular (non-list) response
        data = TimelineEntry.from_json("data/UserTweetsAndReplies.json")

    def test_tweet_detail(self):
        data = TimelineEntry.from_json("data/TweetDetail.json")

    def test_retweeters(self):
        data = TimelineEntry.from_json("data/Retweeters.json")

    def test_favoriters(self):
        data = TimelineEntry.from_json("data/Favoriters.json")


if __name__ == "__main__":
    main()
