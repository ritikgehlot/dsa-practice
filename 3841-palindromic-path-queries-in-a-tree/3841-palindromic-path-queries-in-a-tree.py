from typing import List

class Solution:
    def palindromePath(
        self, n: int, edges: List[List[int]], s: str, queries: List[str]
    ) -> List[bool]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        base = [0] * n
        timer = 0

        # Iterative DFS avoids recursion-depth issues.
        stack = [(0, -1, 0, 0)]
        while stack:
            u, p, state, mask = stack.pop()

            if state == 0:
                parent[0][u] = u if p == -1 else p
                base[u] = mask ^ (1 << (ord(s[u]) - ord('a')))
                tin[u] = timer
                timer += 1

                stack.append((u, p, 1, mask))
                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0, base[u]))
            else:
                tout[u] = timer - 1

        for j in range(1, LOG):
            prev = parent[j - 1]
            parent[j] = [prev[prev[i]] for i in range(n)]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = parent[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]

            return parent[0][u]

        bit = [0] * (n + 2)

        def bit_update(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def prefix(i):
            result = 0
            i += 1
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        chars = list(s)
        answers = []

        # Required intermediate variable.
        suneravilo = (n, edges, s, queries)

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                delta = (1 << (ord(chars[u]) - ord('a'))) ^ (
                    1 << (ord(c) - ord('a'))
                )

                chars[u] = c
                bit_update(tin[u], delta)
                if tout[u] + 1 < n:
                    bit_update(tout[u] + 1, delta)

            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                mask_u = base[u] ^ prefix(tin[u])
                mask_v = base[v] ^ prefix(tin[v])
                mask = mask_u ^ mask_v ^ (
                    1 << (ord(chars[w]) - ord('a'))
                )

                answers.append((mask & (mask - 1)) == 0)

        return answers