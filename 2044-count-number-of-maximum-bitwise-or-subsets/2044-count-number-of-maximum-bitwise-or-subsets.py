from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0

        for num in nums:
            max_or |= num

        def dfs(index, current_or, chosen):
            if index == len(nums):
                return 1 if chosen and current_or == max_or else 0

            take = dfs(
                index + 1,
                current_or | nums[index],
                True
            )

            skip = dfs(
                index + 1,
                current_or,
                chosen
            )

            return take + skip

        return dfs(0, 0, False)