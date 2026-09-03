class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        i = j = 0
        ans = []

        while i < n and j < m:
            if str1[i] == str2[j]:
                ans.append(str1[i])
                i += 1
                j += 1
            elif dp[i + 1][j] >= dp[i][j + 1]:
                ans.append(str1[i])
                i += 1
            else:
                ans.append(str2[j])
                j += 1

        ans.extend(str1[i:])
        ans.extend(str2[j:])

        return ''.join(ans)