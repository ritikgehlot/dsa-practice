class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for total in range(1, target + 1):
            for x in nums:
                if x <= total:
                    dp[total] += dp[total - x]

        return dp[target]