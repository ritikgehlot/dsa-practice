from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        sr = sc = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        k = len(litter)

        if k == 0:
            return 0

        full = (1 << k) - 1

        best = {}
        best[(sr, sc, 0)] = energy

        q = deque([(sr, sc, energy, 0, 0)])

        directions = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        )

        while q:
            r, c, e, mask, dist = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                if e == 0:
                    continue

                ne = e - 1
                nmask = mask

                pos = (nr, nc)

                if pos in litter:
                    nmask |= 1 << litter[pos]

                if nmask == full:
                    return dist + 1

                if classroom[nr][nc] == 'R':
                    ne = energy

                state = (nr, nc, nmask)

                if ne <= best.get(state, -1):
                    continue

                best[state] = ne
                q.append((nr, nc, ne, nmask, dist + 1))

        return -1