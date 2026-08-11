class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                curMax, curMin = curMin, curMax

            curMax = max(num, curMax * num)
            curMin = min(num, curMin * num)

            ans = max(ans, curMax)

        return ans