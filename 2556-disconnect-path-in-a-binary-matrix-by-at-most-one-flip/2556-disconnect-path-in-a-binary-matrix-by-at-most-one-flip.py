class Solution:
    def isPossibleToCutPath(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return True

            grid[r][c] = 0

            if r + 1 < m and grid[r + 1][c] == 1:
                if dfs(r + 1, c):
                    return True

            if c + 1 < n and grid[r][c + 1] == 1:
                if dfs(r, c + 1):
                    return True

            return False

        if not dfs(0, 0):
            return True

        grid[0][0] = 1

        return not dfs(0, 0)