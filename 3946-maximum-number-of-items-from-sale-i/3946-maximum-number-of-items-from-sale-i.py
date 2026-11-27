class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)

        free = [0] * n
        min_price = float('inf')

        for i in range(n):
            factor, price = items[i]
            min_price = min(min_price, price)

            for j in range(n):
                if i != j and items[j][0] % factor == 0:
                    free[i] += 1

        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]
            value = free[i] + 1

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + value)

        ans = 0

        for b in range(budget + 1):
            ans = max(ans, dp[b] + (budget - b) // min_price)

        return ans