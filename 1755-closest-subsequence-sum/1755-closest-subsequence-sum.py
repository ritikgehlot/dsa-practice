from bisect import bisect_left
from typing import List

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        mid = n // 2

        def subset_sums(arr):
            sums = [0]
            for x in arr:
                sums += [s + x for s in sums]
            return sums

        left_sums = subset_sums(nums[:mid])
        right_sums = sorted(subset_sums(nums[mid:]))

        ans = abs(goal)

        for s in left_sums:
            target = goal - s
            i = bisect_left(right_sums, target)

            if i < len(right_sums):
                ans = min(ans, abs(s + right_sums[i] - goal))

            if i > 0:
                ans = min(ans, abs(s + right_sums[i - 1] - goal))

            if ans == 0:
                return 0

        return ans