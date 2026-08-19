from functools import lru_cache

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def shrink(s):
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                if j - i >= 3:
                    return shrink(s[:i] + s[j:])
                i = j
            return s

        @lru_cache(None)
        def dfs(b, h):
            if not b:
                return 0
            best = float('inf')
            for i in range(len(b)):
                for k in range(len(h)):
                    if k > 0 and h[k] == h[k - 1]:
                        continue                      # duplicate ball, already tried
                    same = (h[k] == b[i] and (i == 0 or b[i - 1] != b[i]))
                    split = (i > 0 and b[i - 1] == b[i] and b[i] != h[k])
                    if not (same or split):
                        continue
                    r = dfs(shrink(b[:i] + h[k] + b[i:]), h[:k] + h[k + 1:])
                    if r != float('inf'):
                        best = min(best, r + 1)
            return best

        res = dfs(board, ''.join(sorted(hand)))
        return -1 if res == float('inf') else res