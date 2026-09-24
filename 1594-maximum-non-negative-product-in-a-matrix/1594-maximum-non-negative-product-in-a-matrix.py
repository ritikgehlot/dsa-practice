class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        minimum = [[0] * n for _ in range(m)]
        maximum = [[0] * n for _ in range(m)]

        minimum[0][0] = maximum[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                values = []

                if i > 0:
                    values.append((
                        minimum[i - 1][j] * grid[i][j],
                        maximum[i - 1][j] * grid[i][j]
                    ))

                if j > 0:
                    values.append((
                        minimum[i][j - 1] * grid[i][j],
                        maximum[i][j - 1] * grid[i][j]
                    ))

                candidates = [x for pair in values for x in pair]

                minimum[i][j] = min(candidates)
                maximum[i][j] = max(candidates)

        result = maximum[m - 1][n - 1]

        return result % MOD if result >= 0 else -1