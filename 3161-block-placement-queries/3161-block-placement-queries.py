from typing import List
from bisect import bisect_left

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        coords = sorted({q[1] for q in queries} | {0})
        m = len(coords)
        pos = {x: i for i, x in enumerate(coords)}

        size = 1
        while size < m:
            size *= 2

        tree = [0] * (2 * size)
        obstacles = [0]

        def update(i, val):
            i += size
            tree[i] = val
            i //= 2
            while i:
                tree[i] = max(tree[2 * i], tree[2 * i + 1])
                i //= 2

        def query(l, r):
            res = 0
            l += size
            r += size
            while l < r:
                if l & 1:
                    res = max(res, tree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res = max(res, tree[r])
                l //= 2
                r //= 2
            return res

        update(pos[0], 0)
        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                i = bisect_left(obstacles, x)
                prev = obstacles[i - 1]
                nxt = obstacles[i] if i < len(obstacles) else None

                obstacles.insert(i, x)
                update(pos[x], x - prev)

                if nxt is not None:
                    update(pos[nxt], nxt - x)

            else:
                x, block = q[1], q[2]
                i = bisect_left(obstacles, x)
                prev = obstacles[i - 1] if i > 0 else 0

                end = bisect_left(coords, x)
                best = query(0, end + 1)
                best = max(best, x - prev)

                ans.append(best >= block)

        return ans