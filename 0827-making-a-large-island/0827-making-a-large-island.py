class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        island_area = {}
        island_id = 2

        def dfs(r, c, idx):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0

            if grid[r][c] != 1:
                return 0

            grid[r][c] = idx

            area = 1

            for dr, dc in directions:
                area += dfs(r + dr, c + dc, idx)

            return area

        # Label every island and calculate its area
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_area[island_id] = dfs(r, c, island_id)
                    island_id += 1

        # If the grid is already all 1s
        if len(island_area) == 1:
            only_area = next(iter(island_area.values()))
            if only_area == n * n:
                return only_area

        ans = max(island_area.values(), default=0)

        # Try changing every 0 into 1
        for r in range(n):
            for c in range(n):
                if grid[r][c] != 0:
                    continue

                neighbors = set()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] > 1:
                            neighbors.add(grid[nr][nc])

                current = 1

                for idx in neighbors:
                    current += island_area[idx]

                ans = max(ans, current)

        return ans