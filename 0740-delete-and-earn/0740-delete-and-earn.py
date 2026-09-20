class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        total = [0] * (max(nums) + 1)

        for x in nums:
            total[x] += x

        prev = 0
        curr = 0

        for value in total:
            prev, curr = curr, max(curr, prev + value)

        return curr