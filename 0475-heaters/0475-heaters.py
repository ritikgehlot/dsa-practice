import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()

        ans = 0

        for house in houses:
            i = bisect.bisect_left(heaters, house)

            left = float('inf')
            right = float('inf')

            if i > 0:
                left = house - heaters[i - 1]

            if i < len(heaters):
                right = heaters[i] - house

            ans = max(ans, min(left, right))

        return ans