class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m = len(words[0])
        n = len(target)

        cnt = [[0] * 26 for _ in range(m)]

        for word in words:
            for i, ch in enumerate(word):
                cnt[i][ord(ch) - 97] += 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(m):
            for j in range(min(i + 1, n), 0, -1):
                c = ord(target[j - 1]) - 97
                dp[j] = (dp[j] + dp[j - 1] * cnt[i][c]) % MOD

        return dp[n]