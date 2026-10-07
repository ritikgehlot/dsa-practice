class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, -10**9, -10**9]

        for x in nums:
            ndp = dp[:]

            for r in range(3):
                nr = (r + x) % 3
                ndp[nr] = max(ndp[nr], dp[r] + x)

            dp = ndp

        return dp[0]