from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins = list(set(coins))

        # Remove coins that are multiples of another smaller coin
        useful = []

        for c in sorted(coins):
            if not any(c % x == 0 for x in useful):
                useful.append(c)

        coins = useful

        def count(x):
            # Count how many positive amounts <= x
            # are divisible by at least one coin.
            ans = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        g = gcd(lcm, coins[i])
                        lcm = lcm // g * coins[i]

                        if lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                value = x // lcm

                if bits % 2:
                    ans += value
                else:
                    ans -= value

            return ans

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left