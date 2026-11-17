class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # Precompute the minimum changes needed for every substring.
        cost = [[INF] * n for _ in range(n)]

        for length in range(2, n + 1):
            divisors = [
                d for d in range(1, length)
                if length % d == 0
            ]

            for left in range(n - length + 1):
                right = left + length - 1

                for d in divisors:
                    groups = length // d
                    changes = 0

                    for r in range(d):
                        for t in range(groups // 2):
                            a = left + r + t * d
                            b = left + r + (groups - 1 - t) * d

                            if s[a] != s[b]:
                                changes += 1

                    cost[left][right] = min(
                        cost[left][right], changes
                    )

        # dp[j][i] = minimum changes to divide first i characters
        # into exactly j semi-palindromic substrings.
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):
                for start in range(2 * (parts - 1), end - 1):
                    if dp[parts - 1][start] == INF:
                        continue

                    dp[parts][end] = min(
                        dp[parts][end],
                        dp[parts - 1][start] + cost[start][end - 1]
                    )

        return dp[k][n]