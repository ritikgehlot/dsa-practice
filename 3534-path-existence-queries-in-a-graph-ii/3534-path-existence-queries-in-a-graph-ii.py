class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        order = sorted(range(n), key=lambda i: nums[i])
        pos = [0] * n
        for p, i in enumerate(order):
            pos[i] = p
        vals = [nums[i] for i in order]

        # component id: a gap > maxDiff between neighbours splits components
        comp = [0] * n
        for p in range(1, n):
            comp[p] = comp[p - 1] + (1 if vals[p] - vals[p - 1] > maxDiff else 0)

        # furthest sorted position reachable in one hop
        nxt = [bisect_right(vals, vals[p] + maxDiff) - 1 for p in range(n)]

        LOG = max(1, n.bit_length())
        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[p]] for p in range(n)])

        res = []
        for u, v in queries:
            a, b = sorted((pos[u], pos[v]))
            if a == b:
                res.append(0)
            elif comp[a] != comp[b]:
                res.append(-1)
            else:
                d, cur = 0, a
                for k in range(LOG - 1, -1, -1):
                    if up[k][cur] < b:
                        cur = up[k][cur]
                        d += 1 << k
                res.append(d + 1)
        return res