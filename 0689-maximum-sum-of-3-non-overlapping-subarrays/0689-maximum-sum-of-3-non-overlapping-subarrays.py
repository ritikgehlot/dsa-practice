class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        window = [0] * (n - k + 1)

        for i in range(len(window)):
            window[i] = prefix[i + k] - prefix[i]

        m = len(window)

        # best left index
        left = [0] * m
        best = 0

        for i in range(m):
            if window[i] > window[best]:
                best = i
            left[i] = best

        # best right index
        right = [0] * m
        best = m - 1

        for i in range(m - 1, -1, -1):
            if window[i] >= window[best]:
                best = i
            right[i] = best

        answer = [-1, -1, -1]
        best_sum = -1

        for mid in range(k, m - k):

            l = left[mid - k]
            r = right[mid + k]

            total = window[l] + window[mid] + window[r]

            if total > best_sum:
                best_sum = total
                answer = [l, mid, r]

        return answer