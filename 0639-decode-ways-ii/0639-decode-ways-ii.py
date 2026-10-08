class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7

        def one(c):
            if c == '*':
                return 9
            return 0 if c == '0' else 1

        def two(a, b):
            if a == '*' and b == '*':
                return 15
            if a == '*':
                return 2 if b <= '6' else 1
            if b == '*':
                return 9 if a == '1' else 6 if a == '2' else 0

            return 1 if 10 <= int(a + b) <= 26 else 0

        prev2 = 1
        prev1 = one(s[0])

        for i in range(1, len(s)):
            cur = (
                one(s[i]) * prev1 +
                two(s[i - 1], s[i]) * prev2
            ) % MOD

            prev2, prev1 = prev1, cur

        return prev1