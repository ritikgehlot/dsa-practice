class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n, M = len(nums), max(nums)

        dp = [1 if v <= nums[0] else 0 for v in range(M + 1)]

        for i in range(1, n):
            pre = [0] * (M + 2)
            for v in range(M + 1):
                pre[v + 1] = (pre[v] + dp[v]) % MOD

            ndp = [0] * (M + 1)
            d = nums[i - 1] - nums[i]
            for v in range(nums[i] + 1):
                cap = min(v, v + d)
                if cap >= 0:
                    ndp[v] = pre[min(cap, M) + 1]
            dp = ndp

        return sum(dp) % MOD