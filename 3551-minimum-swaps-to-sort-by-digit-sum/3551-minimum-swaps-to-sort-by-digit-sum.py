from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            return sum(int(d) for d in str(x))

        n = len(nums)
        target = sorted(nums, key=lambda x: (digit_sum(x), x))
        target_index = {num: i for i, num in enumerate(target)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or target_index[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = target_index[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps