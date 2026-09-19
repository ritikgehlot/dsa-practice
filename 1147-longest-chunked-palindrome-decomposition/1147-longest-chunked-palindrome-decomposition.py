class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        left, right = "", ""
        ans = 0

        for i in range(n // 2):
            left += text[i]
            right = text[n - 1 - i] + right
            if left == right:
                ans += 2
                left, right = "", ""

        
        if left or n % 2:
            ans += 1

        return ans