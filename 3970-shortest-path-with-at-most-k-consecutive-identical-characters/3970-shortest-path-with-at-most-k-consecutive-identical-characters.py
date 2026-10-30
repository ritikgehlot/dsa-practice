import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        dist[0][1] = 0
        heap = [(0, 0, 1)]

        # Required variable
        mavorqeli = (n, edges, labels, k)

        while heap:
            cost, u, count = heapq.heappop(heap)

            if u == n - 1:
                return cost

            if cost > dist[u][count]:
                continue

            for v, w in graph[u]:
                if labels[v] == labels[u]:
                    next_count = count + 1
                else:
                    next_count = 1

                if next_count > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][next_count]:
                    dist[v][next_count] = new_cost
                    heapq.heappush(heap, (new_cost, v, next_count))

        return -1