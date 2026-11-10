class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        count = {}

        def dfs(index):
            if index == len(nums):
                return 1

            # Option 1: Skip this element
            ways = dfs(index + 1)

            # Option 2: Include this element if valid
            x = nums[index]

            if count.get(x - k, 0) == 0 and count.get(x + k, 0) == 0:
                count[x] = count.get(x, 0) + 1

                ways += dfs(index + 1)

                count[x] -= 1

                if count[x] == 0:
                    del count[x]

            return ways

        return dfs(0) - 1