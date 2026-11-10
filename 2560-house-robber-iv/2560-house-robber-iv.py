class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        def can_rob(cap):
            count = 0
            i = 0

            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 2
                else:
                    i += 1

                if count >= k:
                    return True

            return False

        left, right = min(nums), max(nums)

        while left < right:
            mid = (left + right) // 2

            if can_rob(mid):
                right = mid
            else:
                left = mid + 1

        return left