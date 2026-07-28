from collections import Counter


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)
        half_parts = []
        mid = ""
        for ch in sorted(cnt):
            c = cnt[ch]
            half_parts.append(ch * (c // 2))
            if c % 2 == 1:
                mid = ch
        first_half = "".join(half_parts)
        return first_half + mid + first_half[::-1]
