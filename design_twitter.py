import heapq
from collections import defaultdict
from typing import List


class DesignTwitter:
    __slots__ = 'time', 'follower_map', 'tweet_map'

    def __init__(self):
        self.time = 0
        self.tweet_map = defaultdict(list)
        self.follower_map = defaultdict(set)

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.tweet_map[user_id].append([self.time, tweet_id])
        self.time -= 1

    def getNewsFeed(self, user_id: int) -> List[int]:
        result, min_heap = [], []
        followees = self.follower_map[user_id]
        self.follower_map[user_id].add(user_id)
        for followee in followees:
            if followee in self.tweet_map:
                index = len(self.tweet_map[followee]) - 1
                recent_time, recent_tweet_id = self.tweet_map[followee][index]
                min_heap.append([recent_time, recent_tweet_id, followee, index - 1])
        heapq.heapify(min_heap)
        while min_heap and len(result) < 10:
            recent_time, recent_tweed_id, followee, index = heapq.heappop(min_heap)
            result.append(recent_tweed_id)
            if index >= 0:
                next_time, next_tweet_id = self.tweet_map[followee][index]
                heapq.heappush(min_heap, [next_time, next_tweet_id, followee, index - 1])
        return result

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.follower_map[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if followee_id in self.follower_map[follower_id]:
            self.follower_map[follower_id].remove(followee_id)


twitter = DesignTwitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))
