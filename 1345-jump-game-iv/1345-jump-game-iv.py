from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = defaultdict(list)

        for i, x in enumerate(arr):
            graph[x].append(i)

        queue = deque([(0, 0)])
        visited = {0}

        while queue:
            i, steps = queue.popleft()

            if i == n - 1:
                return steps

            neighbors = graph[arr[i]]
            neighbors.extend([i - 1, i + 1])

            for j in neighbors:
                if 0 <= j < n and j not in visited:
                    visited.add(j)
                    queue.append((j, steps + 1))

            graph[arr[i]].clear()

        return -1