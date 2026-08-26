class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        dp = [1] * (n + 1)

        for i in range(n):
            new_dp = [0] * (n + 1)

            if s[i] == 'I':
                total = 0

                for j in range(n - i):
                    total = (total + dp[j]) % MOD
                    new_dp[j] = total

            else:  # 'D'
                total = 0

                for j in range(n - i - 1, -1, -1):
                    total = (total + dp[j + 1]) % MOD
                    new_dp[j] = total

            dp = new_dp

        return dp[0]