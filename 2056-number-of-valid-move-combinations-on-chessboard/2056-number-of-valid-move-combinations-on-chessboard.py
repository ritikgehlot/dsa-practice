class Solution:
    def countCombinations(self, pieces: list[str], positions: list[list[int]]) -> int:

        directions = {
            "rook": [
                (0, 1), (0, -1), (1, 0), (-1, 0)
            ],
            "bishop": [
                (1, 1), (1, -1), (-1, 1), (-1, -1)
            ],
            "queen": [
                (0, 1), (0, -1), (1, 0), (-1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1)
            ]
        }

        moves = []

        for piece, (r, c) in zip(pieces, positions):
            options = [(0, 0, 0)]

            for dr, dc in directions[piece]:
                steps = 1

                while (
                    1 <= r + dr * steps <= 8
                    and 1 <= c + dc * steps <= 8
                ):
                    options.append((dr, dc, steps))
                    steps += 1

            moves.append(options)

        paths = []

        def dfs(index):
            if index == len(pieces):
                return 1

            r, c = positions[index]
            ans = 0

            for dr, dc, steps in moves[index]:

                path = []

                for t in range(8):
                    move_time = min(t, steps)

                    x = r + dr * move_time
                    y = c + dc * move_time

                    path.append((x, y))

                valid = True

                for previous in paths:
                    for t in range(1, 8):
                        if path[t] == previous[t]:
                            valid = False
                            break

                    if not valid:
                        break

                if valid:
                    paths.append(path)
                    ans += dfs(index + 1)
                    paths.pop()

            return ans

        return dfs(0)