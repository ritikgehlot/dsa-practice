from functools import lru_cache
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)

        positions = defaultdict(list)

        for i, ch in enumerate(ring):
            positions[ch].append(i)

        @lru_cache(None)
        def dp(pos, index):
            if index == len(key):
                return 0

            ans = float('inf')

            for next_pos in positions[key[index]]:
                distance = abs(next_pos - pos)

                rotation = min(
                    distance,
                    n - distance
                )

                ans = min(
                    ans,
                    rotation + 1 + dp(next_pos, index + 1)
                )

            return ans

        return dp(0, 0)