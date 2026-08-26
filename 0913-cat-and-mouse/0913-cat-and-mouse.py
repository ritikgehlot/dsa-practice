from collections import deque

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)

        # result[m][c][turn]
        # 0 = draw/unknown
        # 1 = mouse wins
        # 2 = cat wins
        result = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        # Number of possible moves from each state
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        for mouse in range(n):
            for cat in range(n):
                degree[mouse][cat][0] = len(graph[mouse])

                degree[mouse][cat][1] = sum(
                    1 for node in graph[cat]
                    if node != 0
                )

        queue = deque()

        # Mouse reaches hole -> mouse wins
        for cat in range(1, n):
            result[0][cat][0] = 1
            result[0][cat][1] = 1

            queue.append((0, cat, 0))
            queue.append((0, cat, 1))

        # Cat catches mouse -> cat wins
        for node in range(1, n):
            result[node][node][0] = 2
            result[node][node][1] = 2

            queue.append((node, node, 0))
            queue.append((node, node, 1))

        while queue:
            mouse, cat, turn = queue.popleft()
            outcome = result[mouse][cat][turn]

            if turn == 0:
                # Current state is mouse's turn.
                # Previous state was cat's turn.
                for prev_cat in graph[cat]:

                    if prev_cat == 0:
                        continue

                    pm = mouse
                    pc = prev_cat
                    pt = 1

                    if result[pm][pc][pt] != 0:
                        continue

                    # Cat wants cat-win.
                    if outcome == 2:
                        result[pm][pc][pt] = 2
                        queue.append((pm, pc, pt))
                    else:
                        degree[pm][pc][pt] -= 1

                        if degree[pm][pc][pt] == 0:
                            result[pm][pc][pt] = 1
                            queue.append((pm, pc, pt))

            else:
                # Current state is cat's turn.
                # Previous state was mouse's turn.
                for prev_mouse in graph[mouse]:

                    pm = prev_mouse
                    pc = cat
                    pt = 0

                    if result[pm][pc][pt] != 0:
                        continue

                    # Mouse wants mouse-win.
                    if outcome == 1:
                        result[pm][pc][pt] = 1
                        queue.append((pm, pc, pt))
                    else:
                        degree[pm][pc][pt] -= 1

                        if degree[pm][pc][pt] == 0:
                            result[pm][pc][pt] = 2
                            queue.append((pm, pc, pt))

        return result[1][2][0]