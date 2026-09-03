class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        left = [[0] * n for _ in range(m)]
        up = [[0] * n for _ in range(m)]

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    left[i][j] = 1 + (left[i][j - 1] if j else 0)
                    up[i][j] = 1 + (up[i - 1][j] if i else 0)

                    size = min(left[i][j], up[i][j])

                    while size > ans:
                        if left[i - size + 1][j] >= size and up[i][j - size + 1] >= size:
                            ans = size
                            break
                        size -= 1

        return ans * ans