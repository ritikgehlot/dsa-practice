from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        count = Counter(s)

        if max(count.values()) > (n + 1) // 2:
            return ""

        ans = [None] * n
        index = 0

        for ch, freq in count.most_common():
            for _ in range(freq):
                ans[index] = ch
                index += 2

                if index >= n:
                    index = 1

        return ''.join(ans)