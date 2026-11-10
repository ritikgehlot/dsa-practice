class Solution:
    def rootCount(self, edges: list[list[int]], guesses: list[list[int]], k: int) -> int:
        n = len(edges) + 1

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        guess_set = {(u, v) for u, v in guesses}

        # Count correct guesses when node 0 is the root.
        parent = [-1] * n
        order = [0]
        parent[0] = 0

        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)

        correct = 0
        for v in range(1, n):
            if (parent[v], v) in guess_set:
                correct += 1

        ans = 0

        # Reroot the tree, updating the number of correct guesses.
        stack = [(0, correct)]

        while stack:
            u, count = stack.pop()

            if count >= k:
                ans += 1

            for v in graph[u]:
                if v == parent[u]:
                    continue

                new_count = count
                if (u, v) in guess_set:
                    new_count -= 1
                if (v, u) in guess_set:
                    new_count += 1

                stack.append((v, new_count))

        return ans