from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        chars = sorted(
            count.keys(),
            key=lambda x: count[x],
            reverse=True
        )

        return ''.join(
            ch * count[ch]
            for ch in chars
        )