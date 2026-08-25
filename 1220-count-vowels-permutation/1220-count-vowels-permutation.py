class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7

        # a, e, i, o, u
        dp = [1, 1, 1, 1, 1]

        for _ in range(1, n):
            a = dp[1] + dp[2] + dp[4]
            e = dp[0] + dp[2]
            i = dp[1] + dp[3]
            o = dp[2]
            u = dp[2] + dp[3]

            dp = [
                a % MOD,
                e % MOD,
                i % MOD,
                o % MOD,
                u % MOD
            ]

        return sum(dp) % MOD