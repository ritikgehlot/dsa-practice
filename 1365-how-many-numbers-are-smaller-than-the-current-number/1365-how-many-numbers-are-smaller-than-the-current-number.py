class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        rank = {}

        for i, x in enumerate(sorted_nums):
            if x not in rank:
                rank[x] = i

        return [rank[x] for x in nums]