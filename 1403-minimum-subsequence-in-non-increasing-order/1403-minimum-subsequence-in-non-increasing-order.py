class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)

        total = sum(nums)
        current = 0
        ans = []

        for x in nums:
            ans.append(x)
            current += x

            if current > total - current:
                break

        return ans