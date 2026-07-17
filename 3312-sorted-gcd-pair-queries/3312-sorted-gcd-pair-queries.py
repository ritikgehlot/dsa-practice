from bisect import bisect_left
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Frequency of each value
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # exact[g] = number of pairs whose gcd is exactly g
        exact = [0] * (mx + 1)

        # Compute exact gcd counts using inclusion-exclusion
        for g in range(mx, 0, -1):
            cnt = 0
            for multiple in range(g, mx + 1, g):
                cnt += freq[multiple]

            pairs = cnt * (cnt - 1) // 2

            for multiple in range(2 * g, mx + 1, g):
                pairs -= exact[multiple]

            exact[g] = pairs

        # Prefix sum of gcd counts
        prefix = [0] * (mx + 1)
        for g in range(1, mx + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        # Answer queries
        ans = []
        for q in queries:
            ans.append(bisect_left(prefix, q + 1, 1))

        return ans