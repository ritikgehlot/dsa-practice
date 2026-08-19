from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for num in nums:
            new_dp = defaultdict(int)

            for total, ways in dp.items():
                new_dp[total + num] += ways
                new_dp[total - num] += ways

            dp = new_dp

        return dp.get(target, 0)