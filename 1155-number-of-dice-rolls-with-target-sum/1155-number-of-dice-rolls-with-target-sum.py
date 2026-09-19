class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1

        for _ in range(n):
            ndp = [0] * (target + 1)

            for s in range(target + 1):
                if dp[s]:
                    for face in range(1, k + 1):
                        if s + face <= target:
                            ndp[s + face] = (ndp[s + face] + dp[s]) % MOD

            dp = ndp

        return dp[target]