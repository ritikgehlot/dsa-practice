from functools import lru_cache
from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        @lru_cache(None)
        def dfs(a, b):
            if a == b:
                return True

            # Different character counts -> impossible
            if Counter(a) != Counter(b):
                return False

            n = len(a)

            for i in range(1, n):
                # No swap
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    return True

                # Swap
                if dfs(a[:i], b[n-i:]) and dfs(a[i:], b[:n-i]):
                    return True

            return False

        return dfs(s1, s2)