class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dp = grid[0][:]

        for i in range(1, n):
            min1 = min(dp)
            idx = dp.index(min1)

            min2 = min(
                dp[j]
                for j in range(n)
                if j != idx
            )

            ndp = [0] * n

            for j in range(n):
                best = min2 if j == idx else min1
                ndp[j] = grid[i][j] + best

            dp = ndp

        return min(dp)