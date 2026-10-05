import heapq

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7

        graph = [[] for _ in range(n + 1)]

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float('inf')] * (n + 1)
        dist[n] = 0

        heap = [(0, n)]

        while heap:
            d, u = heapq.heappop(heap)

            if d > dist[u]:
                continue

            for v, w in graph[u]:
                new_dist = d + w

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

        order = sorted(range(1, n + 1), key=lambda x: dist[x])

        dp = [0] * (n + 1)
        dp[n] = 1

        for u in order:
            for v, w in graph[u]:
                if dist[u] > dist[v]:
                    dp[u] = (dp[u] + dp[v]) % MOD

        return dp[1]