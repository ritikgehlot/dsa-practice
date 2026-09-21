from functools import lru_cache

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        size = n // k
        full = (1 << n) - 1
        INF = 10**9

        groups = []

        for mask in range(1, 1 << n):
            if mask.bit_count() != size:
                continue

            values = []
            seen = set()

            for i in range(n):
                if mask & (1 << i):
                    if nums[i] in seen:
                        break
                    seen.add(nums[i])
                    values.append(nums[i])
            else:
                groups.append((mask, max(values) - min(values)))

        @lru_cache(None)
        def dfs(mask):
            if mask == full:
                return 0

            if mask.bit_count() % size != 0:
                return INF

            first = 0

            for i in range(n):
                if not (mask & (1 << i)):
                    first = i
                    break

            ans = INF

            for group, cost in groups:
                if not (group & (1 << first)):
                    continue

                if group & mask:
                    continue

                ans = min(ans, cost + dfs(mask | group))

            return ans

        result = dfs(0)
        return -1 if result == INF else result