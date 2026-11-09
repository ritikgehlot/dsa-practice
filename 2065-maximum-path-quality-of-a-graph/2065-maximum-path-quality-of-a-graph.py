class Solution:
    def maximalPathQuality(
        self,
        values: list[int],
        edges: list[list[int]],
        maxTime: int
    ) -> int:

        n = len(values)
        graph = [[] for _ in range(n)]

        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        visited = [0] * n
        visited[0] = 1

        ans = 0

        def dfs(node, time, score):
            nonlocal ans

            if node == 0:
                ans = max(ans, score)

            for nxt, cost in graph[node]:
                if time + cost > maxTime:
                    continue

                new_score = score

                if visited[nxt] == 0:
                    new_score += values[nxt]

                visited[nxt] += 1

                dfs(nxt, time + cost, new_score)

                visited[nxt] -= 1

        dfs(0, 0, values[0])

        return ans