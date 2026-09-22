class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                mid = (i + j) // 2
                for t in range(i, j + 1):
                    cost[i][j] += abs(houses[t] - houses[mid])

        INF = 10**9
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for m in range(1, min(k, i) + 1):
                for j in range(m - 1, i):
                    dp[i][m] = min(
                        dp[i][m],
                        dp[j][m - 1] + cost[j][i - 1]
                    )

        return dp[n][k]