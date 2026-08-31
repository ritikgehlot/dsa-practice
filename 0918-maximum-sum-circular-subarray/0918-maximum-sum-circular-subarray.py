class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        max_sum = nums[0]
        current_max = nums[0]

        min_sum = nums[0]
        current_min = nums[0]

        for x in nums[1:]:
            current_max = max(x, current_max + x)
            max_sum = max(max_sum, current_max)

            current_min = min(x, current_min + x)
            min_sum = min(min_sum, current_min)

        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)