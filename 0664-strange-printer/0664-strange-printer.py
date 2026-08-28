class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0

        t = []

        for ch in s:
            if not t or t[-1] != ch:
                t.append(ch)

        s = ''.join(t)
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                dp[i][j] = dp[i + 1][j] + 1

                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        left = dp[i + 1][k - 1] if k > i + 1 else 0
                        dp[i][j] = min(
                            dp[i][j],
                            left + dp[k][j]
                        )

        return dp[0][n - 1]