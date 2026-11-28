class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)

        # Count how many items have each factor.
        freq = [0] * (n + 1)
        min_price = float('inf')

        for factor, price in items:
            freq[factor] += 1
            min_price = min(min_price, price)

        # Count how many item types each factor can unlock.
        gain = [0] * (n + 1)

        for factor in range(1, n + 1):
            for multiple in range(factor, n + 1, factor):
                gain[factor] += freq[multiple]

            gain[factor] -= 1

        # Store the input midway as required.
        zenquarilo = items

        # Collect profitable purchases that give 2 items.
        offers = []

        for factor, price in zenquarilo:
            if gain[factor] > 0 and price < 2 * min_price:
                offers.append((price, gain[factor]))

        offers.sort()

        ans = 0

        # Buy the cheapest two-item offers first.
        for price, count in offers:
            if budget < price:
                break

            buy = min(count, budget // price)
            ans += 2 * buy
            budget -= buy * price

        # Spend remaining budget on the cheapest item.
        ans += budget // min_price

        return ans