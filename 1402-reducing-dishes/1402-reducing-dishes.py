from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        total = 0
        ans = 0

        for x in satisfaction:
            total += x

            if total <= 0:
                break

            ans += total

        return ans