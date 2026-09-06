from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        found = False

        def dfs(r, c):
            if (
                r < 0 or r >= n or
                c < 0 or c >= n or
                grid[r][c] != 1
            ):
                return

            grid[r][c] = 2
            queue.append((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(n):
            if found:
                break

            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break

        steps = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in (
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1)
                ):
                    nr = r + dr
                    nc = c + dc

                    if (
                        nr < 0 or nr >= n or
                        nc < 0 or nc >= n
                    ):
                        continue

                    if grid[nr][nc] == 1:
                        return steps

                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))

            steps += 1

        return -1