class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()

        n = len(nums)

        answer = nums[-1] - nums[0]

        for i in range(n - 1):
            high = max(
                nums[i] + k,
                nums[-1] - k
            )

            low = min(
                nums[0] + k,
                nums[i + 1] - k
            )

            answer = min(answer, high - low)

        return answer