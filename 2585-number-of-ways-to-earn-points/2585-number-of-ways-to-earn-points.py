class Solution:
    def waysToReachTarget(self, target: int, types: list[list[int]]) -> int:
        MOD = 10**9 + 7

        dp = [0] * (target + 1)
        dp[0] = 1

        for count, marks in types:
            ndp = [0] * (target + 1)

            for r in range(marks):
                window = 0

                for score in range(r, target + 1, marks):
                    window += dp[score]

                    remove = score - (count + 1) * marks
                    if remove >= 0:
                        window -= dp[remove]

                    ndp[score] = window % MOD

            dp = ndp

        return dp[target]