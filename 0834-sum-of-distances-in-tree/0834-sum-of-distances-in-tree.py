class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1] * n
        ans = [0] * n

        # First DFS:
        # count[u] = size of subtree of u
        # ans[0] = sum of distances from node 0
        def dfs1(u, parent):
            for v in graph[u]:
                if v == parent:
                    continue

                dfs1(v, u)

                count[u] += count[v]
                ans[u] += ans[v] + count[v]

        # Second DFS:
        # Re-root the tree from u to v
        def dfs2(u, parent):
            for v in graph[u]:
                if v == parent:
                    continue

                ans[v] = ans[u] + n - 2 * count[v]
                dfs2(v, u)

        dfs1(0, -1)
        dfs2(0, -1)

        return ans