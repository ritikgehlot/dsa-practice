class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = maximum = nums[0]

        for num in nums[1:]:
            current = max(num, current + num)
            maximum = max(maximum, current)

        return maximum