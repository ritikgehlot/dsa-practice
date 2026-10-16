from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_a = set()
        seen_b = set()
        ans = []

        common = 0

        for a, b in zip(A, B):
            seen_a.add(a)
            seen_b.add(b)

            if a == b:
                common += 1
            else:
                if b in seen_a:
                    common += 1
                if a in seen_b:
                    common += 1

            ans.append(common)

        return ans