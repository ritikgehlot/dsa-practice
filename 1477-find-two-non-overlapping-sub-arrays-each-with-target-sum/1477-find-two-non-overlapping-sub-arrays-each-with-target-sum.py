class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = 10**9
        best = [INF] * n

        left = 0
        s = 0
        length = INF

        for right in range(n):
            s += arr[right]

            while s > target:
                s -= arr[left]
                left += 1

            if s == target:
                length = min(length, right - left + 1)

            best[right] = length

        ans = INF
        left = 0
        s = 0

        for right in range(n):
            s += arr[right]

            while s > target:
                s -= arr[left]
                left += 1

            if s == target and left > 0 and best[left - 1] < INF:
                ans = min(ans, right - left + 1 + best[left - 1])

        return -1 if ans == INF else ans