class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        n = len(nums)
        mid = (n + 1) // 2

        left = nums[:mid]
        right = nums[mid:]

        ans = []

        for i in range(len(right)):
            ans.append(left[i])
            ans.append(right[i])

        if len(left) > len(right):
            ans.append(left[-1])

        return ans