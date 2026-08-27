from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        if n == 1:
            return 0

        full_mask = (1 << n) - 1

        queue = deque()

        visited = [[False] * (1 << n) for _ in range(n)]

        # Start BFS from every node
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))
            visited[i][mask] = True

        while queue:
            node, mask, distance = queue.popleft()

            for nxt in graph[node]:
                new_mask = mask | (1 << nxt)

                if new_mask == full_mask:
                    return distance + 1

                if not visited[nxt][new_mask]:
                    visited[nxt][new_mask] = True
                    queue.append(
                        (nxt, new_mask, distance + 1)
                    )

        return -1