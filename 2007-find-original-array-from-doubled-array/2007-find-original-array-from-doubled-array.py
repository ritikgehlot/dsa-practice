from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []

        count = Counter(changed)
        ans = []

        for x in sorted(count):
            if count[x] == 0:
                continue

            if x == 0:
                if count[x] % 2 != 0:
                    return []

                ans.extend([0] * (count[x] // 2))
                count[x] = 0

            else:
                if count[2 * x] < count[x]:
                    return []

                ans.extend([x] * count[x])
                count[2 * x] -= count[x]
                count[x] = 0

        return ans