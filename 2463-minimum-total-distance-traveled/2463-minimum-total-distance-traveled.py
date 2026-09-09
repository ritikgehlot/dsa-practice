from functools import cache
from math import inf

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)

        @cache
        def dfs(i, j):
            if i == n:
                return 0

            if j == m:
                return inf

            # Skip this factory
            ans = dfs(i, j + 1)

            # Assign consecutive robots to this factory
            position, limit = factory[j]
            cost = 0

            for k in range(limit):
                if i + k >= n:
                    break

                cost += abs(robot[i + k] - position)

                ans = min(
                    ans,
                    cost + dfs(i + k + 1, j + 1)
                )

            return ans

        return dfs(0, 0)