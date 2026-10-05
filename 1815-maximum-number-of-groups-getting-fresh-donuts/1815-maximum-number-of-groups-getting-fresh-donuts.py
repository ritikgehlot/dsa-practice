from functools import lru_cache

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        cnt = [0] * batchSize
        ans = 0

        for x in groups:
            r = x % batchSize
            if r == 0:
                ans += 1
            else:
                cnt[r] += 1

        @lru_cache(None)
        def dfs(state, rem):
            best = 0
            state = list(state)

            for r in range(1, batchSize):
                if state[r] == 0:
                    continue

                state[r] -= 1

                gain = 1 if rem == 0 else 0
                new_rem = (rem + r) % batchSize

                best = max(
                    best,
                    gain + dfs(tuple(state), new_rem)
                )

                state[r] += 1

            return best

        return ans + dfs(tuple(cnt), 0)