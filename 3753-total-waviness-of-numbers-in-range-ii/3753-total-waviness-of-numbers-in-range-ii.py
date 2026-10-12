from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(x):
            if x <= 0:
                return 0

            digits = list(map(int, str(x)))
            n = len(digits)

            @cache
            def dp(i, prev2, prev1, tight, started):
                if i == n:
                    return (1, 0)

                limit = digits[i] if tight else 9
                count = 0
                total = 0

                for d in range(limit + 1):
                    ntight = tight and d == limit

                    if not started and d == 0:
                        c, w = dp(i + 1, -1, -1, ntight, False)
                    elif not started:
                        c, w = dp(i + 1, -1, d, ntight, True)
                    else:
                        extra = 0
                        if prev2 != -1:
                            if (prev1 > prev2 and prev1 > d) or (
                                prev1 < prev2 and prev1 < d
                            ):
                                extra = 1

                        c, w = dp(i + 1, prev1, d, ntight, True)
                        w += extra * c

                    count += c
                    total += w

                return count, total

            return dp(0, -1, -1, True, False)[1]

        return solve(num2) - solve(num1 - 1)