class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7

        dp = [0] * (n + 1)
        dp[1] = 1

        sharing = 0

        for day in range(2, n + 1):
            if day - delay >= 1:
                sharing += dp[day - delay]

            if day - forget >= 1:
                sharing -= dp[day - forget]

            sharing %= MOD
            dp[day] = sharing

        return sum(dp[max(1, n - forget + 1):n + 1]) % MOD