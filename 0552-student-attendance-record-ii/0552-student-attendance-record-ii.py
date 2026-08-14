class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        # dp[a][l]
        # a = number of absences
        # l = consecutive late days
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1

        for _ in range(n):
            new = [[0] * 3 for _ in range(2)]

            for a in range(2):
                for l in range(3):
                    ways = dp[a][l]

                    if ways == 0:
                        continue

                    # Present
                    new[a][0] = (new[a][0] + ways) % MOD

                    # Late
                    if l < 2:
                        new[a][l + 1] = (
                            new[a][l + 1] + ways
                        ) % MOD

                    # Absent
                    if a == 0:
                        new[1][0] = (
                            new[1][0] + ways
                        ) % MOD

            dp = new

        return sum(map(sum, dp)) % MOD