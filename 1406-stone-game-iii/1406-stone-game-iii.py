from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        @lru_cache(None)
        def dfs(i):
            if i >= len(stoneValue):
                return 0

            best = float("-inf")
            total = 0

            for j in range(i, min(i + 3, len(stoneValue))):
                total += stoneValue[j]
                best = max(best, total - dfs(j + 1))

            return best

        diff = dfs(0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"