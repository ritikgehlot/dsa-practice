class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        if n <= 2:
            return n

        a, b, c = 1, 1, 2

        for _ in range(3, n + 1):
            a, b, c = b, c, (2 * c + a) % MOD

        return c