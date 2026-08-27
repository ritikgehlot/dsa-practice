class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Make first column all 1
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1

        answer = 0

        for j in range(n):
            ones = 0

            for i in range(m):
                ones += grid[i][j]

            ones = max(ones, m - ones)

            answer += ones * (1 << (n - j - 1))

        return answer