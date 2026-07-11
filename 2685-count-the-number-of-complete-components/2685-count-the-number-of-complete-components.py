from typing import List


class Solution:
    def countCompleteComponents(
        self,
        n: int,
        edges: List[List[int]]
    ) -> int:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        answer = 0

        def dfs(node):
            visited[node] = True

            vertex_count = 1
            degree_sum = len(graph[node])

            for neighbour in graph[node]:
                if not visited[neighbour]:
                    child_vertices, child_degrees = dfs(neighbour)

                    vertex_count += child_vertices
                    degree_sum += child_degrees

            return vertex_count, degree_sum

        for node in range(n):
            if not visited[node]:
                vertices, degree_sum = dfs(node)

                actual_edges = degree_sum // 2
                required_edges = vertices * (vertices - 1) // 2

                if actual_edges == required_edges:
                    answer += 1

        return answer