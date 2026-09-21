from bisect import bisect_left

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        left = [1] * n
        tails = []

        for i in range(n):
            pos = bisect_left(tails, nums[i])

            if pos == len(tails):
                tails.append(nums[i])
            else:
                tails[pos] = nums[i]

            left[i] = pos + 1

        right = [1] * n
        tails = []

        for i in range(n - 1, -1, -1):
            pos = bisect_left(tails, nums[i])

            if pos == len(tails):
                tails.append(nums[i])
            else:
                tails[pos] = nums[i]

            right[i] = pos + 1

        best = 0

        for i in range(1, n - 1):
            if left[i] > 1 and right[i] > 1:
                best = max(best, left[i] + right[i] - 1)

        return n - best