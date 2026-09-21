from collections import Counter
from functools import lru_cache

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        counts = tuple(sorted(Counter(nums).values(), reverse=True))
        quantity.sort(reverse=True)

        @lru_cache(None)
        def dfs(i, capacities):
            if i == len(quantity):
                return True

            q = quantity[i]
            used = set()

            for j in range(len(capacities)):
                if capacities[j] < q:
                    continue

                if capacities[j] in used:
                    continue

                used.add(capacities[j])

                new_capacities = list(capacities)
                new_capacities[j] -= q
                new_capacities.sort(reverse=True)

                if dfs(i + 1, tuple(new_capacities)):
                    return True

            return False

        return dfs(0, counts)