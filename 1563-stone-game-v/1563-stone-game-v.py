from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(left, right):
            if left >= right:
                return 0

            ans = 0
            left_sum = 0
            right_sum = prefix[right + 1] - prefix[left]

            for i in range(left, right):
                left_sum += stoneValue[i]
                right_sum -= stoneValue[i]

                if left_sum < right_sum:
                    # Maximum possible score from this split
                    # cannot beat ans if ans >= 2 * left_sum
                    if ans >= 2 * left_sum:
                        continue

                    ans = max(
                        ans,
                        left_sum + dfs(left, i)
                    )

                elif left_sum > right_sum:
                    # Since right_sum will only decrease from here,
                    # we can stop when this cannot improve ans.
                    if ans >= 2 * right_sum:
                        break

                    ans = max(
                        ans,
                        right_sum + dfs(i + 1, right)
                    )

                else:
                    ans = max(
                        ans,
                        left_sum + dfs(left, i),
                        right_sum + dfs(i + 1, right)
                    )

            return ans

        return dfs(0, len(stoneValue) - 1)