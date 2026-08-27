class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        dp = [set() for _ in range(n // 2 + 1)]
        dp[0].add(0)

        for num in nums:
            for size in range(n // 2, 0, -1):
                for total_sum in list(dp[size - 1]):
                    dp[size].add(total_sum + num)

        for size in range(1, n // 2 + 1):
            if (total * size) % n == 0:
                target = (total * size) // n

                if target in dp[size]:
                    return True

        return False