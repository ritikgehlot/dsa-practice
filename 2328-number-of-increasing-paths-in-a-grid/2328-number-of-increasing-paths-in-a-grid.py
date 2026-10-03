from functools import lru_cache

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        @lru_cache(None)
        def dfs(i, j):
            ans = 1

            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj

                if (
                    0 <= ni < m and
                    0 <= nj < n and
                    grid[ni][nj] > grid[i][j]
                ):
                    ans += dfs(ni, nj)

            return ans % MOD

        return sum(
            dfs(i, j)
            for i in range(m)
            for j in range(n)
        ) % MOD