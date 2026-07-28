from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = defaultdict(int)

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0:
                    key = (0, 1)          # vertical
                elif dy == 0:
                    key = (1, 0)          # horizontal
                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g

                    # normalize sign
                    if dx < 0:
                        dx *= -1
                        dy *= -1

                    key = (dx, dy)

                slopes[key] += 1
                ans = max(ans, slopes[key] + 1)

        return ans