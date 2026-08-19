from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        if total < desiredTotal:
            return False

        if desiredTotal <= 0:
            return True

        @lru_cache(None)
        def dfs(mask, current):
            for num in range(1, maxChoosableInteger + 1):
                bit = 1 << (num - 1)

                if mask & bit:
                    continue

                # Take num and win immediately
                if current + num >= desiredTotal:
                    return True

                # Make the opponent lose
                if not dfs(mask | bit, current + num):
                    return True

            return False

        return dfs(0, 0)