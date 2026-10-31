from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # Cache the final empty cell reached after all reflections.
        memo = {}

        def resolve(r, c, direction):
            path = []

            while 0 <= r < m and 0 <= c < n:
                state = (r, c, direction)

                if state in memo:
                    result = memo[state]
                    break

                # Stop when an empty cell is reached.
                if grid[r][c] == 0:
                    result = (r, c)
                    memo[state] = result
                    break

                path.append(state)

                # Direction 0 = right; direction 1 = down.
                if direction == 0:
                    # Right into mirror -> turn down.
                    r += 1
                    direction = 1
                else:
                    # Down into mirror -> turn right.
                    c += 1
                    direction = 0
            else:
                result = None

            # Cache all intermediate mirror states.
            for state in path:
                memo[state] = result

            return result

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or dp[i][j] == 0:
                    continue

                if (i, j) == (m - 1, n - 1):
                    continue

                ways = dp[i][j]

                # Try moving right.
                dest = resolve(i, j + 1, 0)
                if dest is not None:
                    x, y = dest
                    dp[x][y] = (dp[x][y] + ways) % MOD

                # Try moving down.
                dest = resolve(i + 1, j, 1)
                if dest is not None:
                    x, y = dest
                    dp[x][y] = (dp[x][y] + ways) % MOD

        return dp[m - 1][n - 1]