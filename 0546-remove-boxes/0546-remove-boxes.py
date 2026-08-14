from functools import lru_cache

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0

            # Merge boxes with the same color at the beginning.
            while l < r and boxes[l] == boxes[l + 1]:
                l += 1
                k += 1

            # Remove this group now.
            best = (k + 1) * (k + 1) + dp(l + 1, r, 0)

            # Try to merge boxes[l] with another same-colored box.
            for i in range(l + 1, r + 1):
                if boxes[i] == boxes[l]:
                    best = max(
                        best,
                        dp(l + 1, i - 1, 0) +
                        dp(i, r, k + 1)
                    )

            return best

        return dp(0, len(boxes) - 1, 0)