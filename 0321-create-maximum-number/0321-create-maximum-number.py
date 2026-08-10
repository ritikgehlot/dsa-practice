class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def get_max(nums, k):
            drop = len(nums) - k
            stack = []

            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1

                stack.append(num)

            return stack[:k]

        def greater(a, i, b, j):
            while i < len(a) and j < len(b):
                if a[i] != b[j]:
                    return a[i] > b[j]
                i += 1
                j += 1

            return i != len(a)

        def merge(a, b):
            res = []
            i = j = 0

            while i < len(a) or j < len(b):
                if greater(a, i, b, j):
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1

            return res

        ans = []

        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            a = get_max(nums1, i)
            b = get_max(nums2, k - i)

            candidate = merge(a, b)

            if candidate > ans:
                ans = candidate

        return ans