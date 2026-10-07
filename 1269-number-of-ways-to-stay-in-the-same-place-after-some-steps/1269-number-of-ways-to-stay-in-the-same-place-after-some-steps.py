class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        n = min(arrLen, steps + 1)

        dp = [0] * n
        dp[0] = 1

        for _ in range(steps):
            ndp = [0] * n

            for i in range(n):
                ndp[i] = dp[i]

                if i > 0:
                    ndp[i] += dp[i - 1]

                if i + 1 < n:
                    ndp[i] += dp[i + 1]

                ndp[i] %= MOD

            dp = ndp

        return dp[0]