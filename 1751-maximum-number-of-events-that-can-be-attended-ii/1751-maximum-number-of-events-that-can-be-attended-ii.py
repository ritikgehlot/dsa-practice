from bisect import bisect_right
from functools import lru_cache
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        starts = [event[0] for event in events]

        @lru_cache(None)
        def dp(i, remaining):
            if i == n or remaining == 0:
                return 0

            skip = dp(i + 1, remaining)

            next_i = bisect_right(starts, events[i][1])
            attend = events[i][2] + dp(next_i, remaining - 1)

            return max(skip, attend)

        return dp(0, k)