from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        a = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)],
            key=lambda x: (x[1], x[0], x[3])
        )

        n = len(a)
        ends = [x[1] for x in a]

        prev = [
            bisect_left(ends, a[i][0], 0, i) - 1
            for i in range(n)
        ]

        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(1, n + 1):
                skip = dp[k][i - 1]

                j = prev[i - 1] + 1
                base = dp[k - 1][j]

                take = (
                    base[0] + a[i - 1][2],
                    sorted(base[1] + [a[i - 1][3]])
                )

                if take[0] > skip[0]:
                    dp[k][i] = take
                elif take[0] < skip[0]:
                    dp[k][i] = skip
                else:
                    dp[k][i] = min(take, skip)

        return dp[4][n][1]