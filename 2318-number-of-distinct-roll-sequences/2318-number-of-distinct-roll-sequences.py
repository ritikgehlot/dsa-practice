from math import gcd

class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 6

        dp = [[0] * 7 for _ in range(7)]

        for a in range(1, 7):
            for b in range(1, 7):
                if a != b and gcd(a, b) == 1:
                    dp[a][b] = 1

        for _ in range(3, n + 1):
            ndp = [[0] * 7 for _ in range(7)]

            for prev in range(1, 7):
                for last in range(1, 7):
                    if dp[prev][last] == 0:
                        continue

                    for nxt in range(1, 7):
                        if nxt != last and gcd(nxt, last) == 1 and nxt != prev:
                            ndp[last][nxt] += dp[prev][last]
                            ndp[last][nxt] %= MOD

            dp = ndp

        return sum(map(sum, dp)) % MOD