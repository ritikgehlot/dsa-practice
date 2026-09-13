class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0.0] * (query_row + 2)
        dp[0] = poured

        for row in range(query_row):
            next_row = [0.0] * (query_row + 2)

            for j in range(row + 1):
                overflow = max(0.0, (dp[j] - 1) / 2)

                next_row[j] += overflow
                next_row[j + 1] += overflow

            dp = next_row

        return min(1.0, dp[query_glass])