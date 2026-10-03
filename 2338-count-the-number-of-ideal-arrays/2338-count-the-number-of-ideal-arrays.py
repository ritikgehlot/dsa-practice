class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        MAX = 14

        comb = [[0] * MAX for _ in range(n)]

        for i in range(n):
            comb[i][0] = 1
            for j in range(1, min(i, MAX - 1) + 1):
                comb[i][j] = (
                    comb[i - 1][j - 1] + comb[i - 1][j]
                ) % MOD

        dp = [[0] * (MAX + 1) for _ in range(maxValue + 1)]

        for x in range(1, maxValue + 1):
            dp[x][1] = 1

        for length in range(1, MAX):
            for x in range(1, maxValue + 1):
                if dp[x][length] == 0:
                    continue

                for y in range(x * 2, maxValue + 1, x):
                    dp[y][length + 1] = (
                        dp[y][length + 1] + dp[x][length]
                    ) % MOD

        ans = 0

        for x in range(1, maxValue + 1):
            for length in range(1, MAX + 1):
                ans = (
                    ans + dp[x][length] * comb[n - 1][length - 1]
                ) % MOD

        return ans