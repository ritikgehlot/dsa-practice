class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        INF = 10**9

        dp = [1, 0, 1]

        for obstacle in obstacles[1:]:
            if obstacle:
                dp[obstacle - 1] = INF

            for i in range(3):
                if obstacle != i + 1:
                    dp[i] = min(
                        dp[i],
                        dp[(i + 1) % 3] + 1,
                        dp[(i + 2) % 3] + 1
                    )

        return min(dp)