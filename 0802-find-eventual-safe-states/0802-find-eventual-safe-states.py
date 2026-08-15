class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n

        def dfs(node):
            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            if state[node] == 3:
                return False

            state[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    state[node] = 3
                    return False

            state[node] = 2
            return True

        ans = []

        for i in range(n):
            if dfs(i):
                ans.append(i)

        return ans