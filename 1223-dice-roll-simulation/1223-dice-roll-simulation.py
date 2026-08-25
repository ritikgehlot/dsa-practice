class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7

        # dp[d][r] = number of sequences ending with
        # face d appearing exactly r times consecutively
        dp = [[0] * 16 for _ in range(6)]

        for d in range(6):
            dp[d][1] = 1

        for _ in range(1, n):
            new_dp = [[0] * 16 for _ in range(6)]

            for last in range(6):
                for count in range(1, rollMax[last] + 1):

                    ways = dp[last][count]

                    if ways == 0:
                        continue

                    for nxt in range(6):

                        if nxt == last:
                            if count + 1 <= rollMax[last]:
                                new_dp[nxt][count + 1] += ways
                                new_dp[nxt][count + 1] %= MOD
                        else:
                            new_dp[nxt][1] += ways
                            new_dp[nxt][1] %= MOD

            dp = new_dp

        ans = 0

        for d in range(6):
            for count in range(1, rollMax[d] + 1):
                ans += dp[d][count]

        return ans % MOD