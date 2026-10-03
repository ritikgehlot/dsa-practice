class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def kadane(a, b):
            best = cur = 0

            for x, y in zip(a, b):
                cur = max(0, cur + y - x)
                best = max(best, cur)

            return best

        sum1 = sum(nums1)
        sum2 = sum(nums2)

        gain1 = kadane(nums1, nums2)
        gain2 = kadane(nums2, nums1)

        return max(sum1 + gain1, sum2 + gain2)