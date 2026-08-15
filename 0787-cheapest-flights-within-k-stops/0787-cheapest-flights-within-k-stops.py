class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0

        for _ in range(k + 1):
            new_dist = dist[:]

            for u, v, price in flights:
                if dist[u] != INF:
                    new_dist[v] = min(
                        new_dist[v],
                        dist[u] + price
                    )

            dist = new_dist

        return -1 if dist[dst] == INF else dist[dst]