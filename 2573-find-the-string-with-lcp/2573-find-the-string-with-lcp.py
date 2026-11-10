class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        n = len(lcp)
        ans = [''] * n
        letters = 'abcdefghijklmnopqrstuvwxyz'
        next_char = 0

        for i in range(n):
            if ans[i] == '':
                if next_char == 26:
                    return ""

                ans[i] = letters[next_char]
                next_char += 1

            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    if ans[j] and ans[j] != ans[i]:
                        return ""
                    ans[j] = ans[i]

        # Verify the complete LCP matrix.
        s = ''.join(ans)
        actual = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    actual[i][j] = 1 + actual[i + 1][j + 1]

                if actual[i][j] != lcp[i][j]:
                    return ""

        return s