class Solution:
    def squareFreeSubsets(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        freq = [0] * 31
        for x in nums:
            freq[x] += 1

        dp = [0] * (1 << 10)
        dp[0] = 1

        ones = freq[1]

        for x in range(2, 31):
            if freq[x] == 0:
                continue

            mask = 0
            valid = True

            for j, p in enumerate(primes):
                if x % (p * p) == 0:
                    valid = False
                    break
                if x % p == 0:
                    mask |= 1 << j

            if not valid:
                continue

            ndp = dp[:]

            for state in range(1 << 10):
                if state & mask == 0:
                    new_state = state | mask
                    ndp[new_state] = (
                        ndp[new_state] + dp[state] * freq[x]
                    ) % MOD

            dp = ndp

        return (sum(dp) * pow(2, ones, MOD) - 1) % MOD