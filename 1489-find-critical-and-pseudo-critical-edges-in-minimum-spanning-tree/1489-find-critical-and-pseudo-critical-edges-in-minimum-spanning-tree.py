class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:

        indexed = [
            [u, v, w, i]
            for i, (u, v, w) in enumerate(edges)
        ]

        indexed.sort(key=lambda x: x[2])

        def mst(skip=-1, force=-1):
            parent = list(range(n))
            rank = [0] * n
            total = 0
            count = 0

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(a, b):
                ra, rb = find(a), find(b)

                if ra == rb:
                    return False

                if rank[ra] < rank[rb]:
                    ra, rb = rb, ra

                parent[rb] = ra

                if rank[ra] == rank[rb]:
                    rank[ra] += 1

                return True

            if force != -1:
                u, v, w, _ = indexed[force]
                if union(u, v):
                    total += w
                    count += 1

            for i, (u, v, w, _) in enumerate(indexed):
                if i == skip or i == force:
                    continue

                if union(u, v):
                    total += w
                    count += 1

            if count == n - 1:
                return total

            return float("inf")

        original = mst()
        critical = []
        pseudo = []

        for i in range(len(indexed)):
            if mst(skip=i) > original:
                critical.append(indexed[i][3])
            elif mst(force=i) == original:
                pseudo.append(indexed[i][3])

        return [critical, pseudo]