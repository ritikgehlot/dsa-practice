from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                      queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(current, target, visited):
            if current not in graph or target not in graph:
                return -1.0

            if current == target:
                return 1.0

            visited.add(current)

            for nxt, value in graph[current]:
                if nxt not in visited:
                    result = dfs(nxt, target, visited)

                    if result != -1.0:
                        return value * result

            return -1.0

        answer = []

        for a, b in queries:
            answer.append(dfs(a, b, set()))

        return answer