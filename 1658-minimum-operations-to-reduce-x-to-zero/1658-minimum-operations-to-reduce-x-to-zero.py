class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)

        if target < 0:
            return -1

        if target == 0:
            return n

        left = 0
        current = 0
        longest = -1

        for right in range(n):
            current += nums[right]

            while current > target and left <= right:
                current -= nums[left]
                left += 1

            if current == target:
                longest = max(longest, right - left + 1)

        return -1 if longest == -1 else n - longest