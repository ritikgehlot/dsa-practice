class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()

        dp0 = 1  # Longest sequence ending at the current value
        dp1 = 1  # Longest sequence ending at current value + 1
        ans = 1

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]

            if diff == 0:
                dp1 = dp0 + 1

            elif diff == 1:
                dp0 += 1
                dp1 += 1

            elif diff == 2:
                dp0 = dp1 + 1
                dp1 = 1

            else:
                dp0 = 1
                dp1 = 1

            ans = max(ans, dp0, dp1)

        return ans