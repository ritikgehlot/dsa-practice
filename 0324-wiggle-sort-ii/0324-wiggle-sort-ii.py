class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()

        n = len(nums)
        mid = (n + 1) // 2

        small = nums[:mid][::-1]
        large = nums[mid:][::-1]

        j = 0

        for i in range(0, n, 2):
            nums[i] = small[j]
            j += 1

        j = 0

        for i in range(1, n, 2):
            nums[i] = large[j]
            j += 1