from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        frequencies = sorted(count.values(), reverse=True)

        removed = 0
        ans = 0
        target = len(arr) // 2

        for freq in frequencies:
            removed += freq
            ans += 1

            if removed >= target:
                return ans

        return ans