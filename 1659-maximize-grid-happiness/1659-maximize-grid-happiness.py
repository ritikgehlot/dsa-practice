from functools import lru_cache

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        if m > n:
            m, n = n, m

        states = 3 ** n
        digits = [[0] * n for _ in range(states)]
        intro = [0] * states
        extro = [0] * states
        base = [0] * states

        for state in range(states):
            x = state
            for j in range(n):
                digits[state][j] = x % 3
                x //= 3

            for j in range(n):
                if digits[state][j] == 1:
                    intro[state] += 1
                    base[state] += 120
                elif digits[state][j] == 2:
                    extro[state] += 1
                    base[state] += 40

        def interaction(a, b):
            if a == 0 or b == 0:
                return 0
            if a == 1 and b == 1:
                return -60
            if a == 2 and b == 2:
                return 40
            return -10

        gain = [[0] * states for _ in range(states)]

        for prev in range(states):
            for cur in range(states):
                total = 0
                for j in range(n):
                    total += interaction(
                        digits[prev][j],
                        digits[cur][j]
                    )
                    if j > 0:
                        total += interaction(
                            digits[cur][j - 1],
                            digits[cur][j]
                        )
                gain[prev][cur] = total

        @lru_cache(None)
        def dfs(row, prev, intro_left, extro_left):
            if row == m:
                return 0

            ans = 0

            for cur in range(states):
                if intro[cur] > intro_left or extro[cur] > extro_left:
                    continue

                score = base[cur] + gain[prev][cur]

                ans = max(
                    ans,
                    score + dfs(
                        row + 1,
                        cur,
                        intro_left - intro[cur],
                        extro_left - extro[cur]
                    )
                )

            return ans

        return dfs(0, 0, introvertsCount, extrovertsCount)