from collections import defaultdict
from bisect import bisect_left

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        pos = defaultdict(list)

        for i, x in enumerate(nums):
            pos[x].append(i)

        n = len(nums)
        ans = []

        for q in queries:
            arr = pos[nums[q]]

            if len(arr) == 1:
                ans.append(-1)
                continue

            i = bisect_left(arr, q)

            left = arr[i - 1] if i > 0 else arr[-1]
            right = arr[i + 1] if i + 1 < len(arr) else arr[0]

            d1 = abs(q - left)
            d2 = abs(right - q)

            d1 = min(d1, n - d1)
            d2 = min(d2, n - d2)

            ans.append(min(d1, d2))

        return ans