class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # Binary search hamesha smaller array par karenge
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m

        while low <= high:
            # nums1 aur nums2 ke partition points
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Partition boundaries
            maxLeft1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float("inf") if partition1 == m else nums1[partition1]

            maxLeft2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float("inf") if partition2 == n else nums2[partition2]

            # Correct partition mil gaya
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:

                # Total elements odd hain
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))

                # Total elements even hain
                leftMaximum = max(maxLeft1, maxLeft2)
                rightMinimum = min(minRight1, minRight2)

                return (leftMaximum + rightMinimum) / 2.0

            # nums1 ka partition bahut right side par hai
            elif maxLeft1 > minRight2:
                high = partition1 - 1

            # nums1 ka partition bahut left side par hai
            else:
                low = partition1 + 1

        return 0.0