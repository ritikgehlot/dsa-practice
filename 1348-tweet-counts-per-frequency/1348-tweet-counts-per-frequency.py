from collections import defaultdict
from bisect import bisect_left, bisect_right

class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(
        self,
        freq: str,
        tweetName: str,
        startTime: int,
        endTime: int
    ) -> List[int]:

        interval = {
            "minute": 60,
            "hour": 3600,
            "day": 86400
        }[freq]

        times = sorted(self.tweets[tweetName])

        ans = []

        start = startTime

        while start <= endTime:
            end = min(start + interval - 1, endTime)

            left = bisect_left(times, start)
            right = bisect_right(times, end)

            ans.append(right - left)

            start += interval

        return ans