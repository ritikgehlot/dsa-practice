class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seen = set(nums)

        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        while total in seen:
            total += 1

        return total