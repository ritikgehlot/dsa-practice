from collections import Counter

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        MAX = 1 << 10
        INF = 10**9

        dp = [INF] * MAX
        dp[0] = 0

        for i in range(k):
            group = nums[i::k]
            cnt = Counter(group)
            size = len(group)

            ndp = [min(dp) + size] * MAX

            for x, frequency in cnt.items():
                for prev in range(MAX):
                    ndp[prev ^ x] = min(
                        ndp[prev ^ x],
                        dp[prev] + size - frequency
                    )

            dp = ndp

        return dp[0]