class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m = len(cost)
        n = len(cost[0])
        INF = 10**9

        dp = [[INF] * (1 << n) for _ in range(m + 1)]
        dp[0][0] = 0

        for i in range(m):
            for mask in range(1 << n):
                if dp[i][mask] == INF:
                    continue

                for j in range(n):
                    new_mask = mask | (1 << j)
                    dp[i + 1][new_mask] = min(
                        dp[i + 1][new_mask],
                        dp[i][mask] + cost[i][j]
                    )

        min_cost = [INF] * (1 << n)

        for mask in range(1 << n):
            min_cost[mask] = dp[m][mask]

        for j in range(n):
            best = min(cost[i][j] for i in range(m))

            for mask in range(1 << n):
                if mask & (1 << j) == 0:
                    min_cost[mask | (1 << j)] = min(
                        min_cost[mask | (1 << j)],
                        min_cost[mask] + best
                    )

        return min_cost[(1 << n) - 1]