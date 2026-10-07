class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        cost = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                cost[l][r] = cost[l + 1][r - 1] + (s[l] != s[r])

        INF = 10**9
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for parts in range(1, min(k, i) + 1):
                for j in range(parts - 1, i):
                    dp[i][parts] = min(
                        dp[i][parts],
                        dp[j][parts - 1] + cost[j][i - 1]
                    )

        return dp[n][k]