from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])

        start_r = 0
        start_c = 0
        key_count = 0

        for r in range(m):
            for c in range(n):
                ch = grid[r][c]

                if ch == '@':
                    start_r = r
                    start_c = c

                elif 'a' <= ch <= 'f':
                    key_count += 1

        full_mask = (1 << key_count) - 1

        queue = deque([
            (start_r, start_c, 0, 0)
        ])

        visited = set()
        visited.add((start_r, start_c, 0))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            r, c, mask, steps = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                ch = grid[nr][nc]

                if ch == '#':
                    continue

                new_mask = mask

                # Key
                if 'a' <= ch <= 'f':
                    new_mask |= 1 << (ord(ch) - ord('a'))

                # Lock
                if 'A' <= ch <= 'F':
                    key_bit = 1 << (ord(ch) - ord('A'))

                    if not (mask & key_bit):
                        continue

                if new_mask == full_mask:
                    return steps + 1

                state = (nr, nc, new_mask)

                if state not in visited:
                    visited.add(state)
                    queue.append(
                        (nr, nc, new_mask, steps + 1)
                    )

        return -1