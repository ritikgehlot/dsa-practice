from math import gcd
from functools import lru_cache

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(mask):
            if mask == (1 << n) - 1:
                return 0

            operation = mask.bit_count() // 2 + 1
            ans = 0

            for i in range(n):
                if mask & (1 << i):
                    continue

                for j in range(i + 1, n):
                    if mask & (1 << j):
                        continue

                    new_mask = mask | (1 << i) | (1 << j)

                    ans = max(
                        ans,
                        operation * gcd(nums[i], nums[j]) + dfs(new_mask)
                    )

            return ans

        return dfs(0)