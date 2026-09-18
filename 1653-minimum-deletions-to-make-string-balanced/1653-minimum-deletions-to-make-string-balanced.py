class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = 0
        ans = 0

        for ch in s:
            if ch == 'b':
                b += 1
            else:
                ans = min(ans + 1, b)

        return ans