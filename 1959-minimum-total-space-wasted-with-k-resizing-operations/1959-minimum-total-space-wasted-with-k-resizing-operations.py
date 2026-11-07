class Solution:
    def minSpaceWastedKResizing(self, nums: list[int], k: int) -> int:
        n = len(nums)
        INF = float('inf')

        dp = [[INF] * (k + 2) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            max_val = 0
            total = 0

            for j in range(i - 1, -1, -1):
                max_val = max(max_val, nums[j])
                total += nums[j]

                waste = max_val * (i - j) - total

                for used in range(1, k + 2):
                    if dp[j][used - 1] != INF:
                        dp[i][used] = min(
                            dp[i][used],
                            dp[j][used - 1] + waste
                        )

        return min(dp[n])