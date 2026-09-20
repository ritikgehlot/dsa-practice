class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        next_same = [n] * n
        prev_same = [-1] * n

        last = [-1] * 4

        for i in range(n):
            c = ord(s[i]) - ord('a')
            prev_same[i] = last[c]
            last[c] = i

        last = [n] * 4

        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - ord('a')
            next_same[i] = last[c]
            last[c] = i

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r]:
                    left = next_same[l]
                    right = prev_same[r]

                    if left > right:
                        dp[l][r] = 2 * dp[l + 1][r - 1] + 2
                    elif left == right:
                        dp[l][r] = 2 * dp[l + 1][r - 1] + 1
                    else:
                        dp[l][r] = (
                            2 * dp[l + 1][r - 1]
                            - dp[left + 1][right - 1]
                        )
                else:
                    dp[l][r] = (
                        dp[l + 1][r]
                        + dp[l][r - 1]
                        - dp[l + 1][r - 1]
                    )

                dp[l][r] %= MOD

        return dp[0][n - 1]