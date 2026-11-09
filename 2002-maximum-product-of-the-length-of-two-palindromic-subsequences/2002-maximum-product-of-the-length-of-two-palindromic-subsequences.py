class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        total = 1 << n

        pal = [0] * total

        for mask in range(1, total):
            chars = [s[i] for i in range(n) if mask & (1 << i)]
            pal[mask] = len(chars) if chars == chars[::-1] else 0

        best = pal[:]

        # best[mask] = longest palindromic subsequence
        # contained in mask
        for mask in range(total):
            for i in range(n):
                if mask & (1 << i):
                    best[mask] = max(
                        best[mask],
                        best[mask ^ (1 << i)]
                    )

        ans = 0
        full = total - 1

        for mask in range(total):
            ans = max(
                ans,
                pal[mask] * best[full ^ mask]
            )

        return ans