class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)

            if ra == rb:
                return False

            parent[rb] = ra
            return True

        groups = n

        for i in range(n):
            for j in range(i + 1, n):
                diff = 0

                for a, b in zip(strs[i], strs[j]):
                    if a != b:
                        diff += 1

                        if diff > 2:
                            break

                # Similar if identical or exactly 2 positions differ
                if diff == 0 or diff == 2:
                    if union(i, j):
                        groups -= 1

        return groups