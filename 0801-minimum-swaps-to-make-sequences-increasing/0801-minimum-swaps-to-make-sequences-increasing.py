class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        keep = 0
        swap = 1

        for i in range(1, len(nums1)):
            nk = float('inf')
            ns = float('inf')

            if nums1[i - 1] < nums1[i] and nums2[i - 1] < nums2[i]:
                nk = keep
                ns = swap + 1

            if nums1[i - 1] < nums2[i] and nums2[i - 1] < nums1[i]:
                nk = min(nk, swap)
                ns = min(ns, keep + 1)

            keep, swap = nk, ns

        return min(keep, swap)