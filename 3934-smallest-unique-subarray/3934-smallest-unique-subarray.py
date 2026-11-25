from collections import defaultdict

class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        base1, mod1 = 233, 998244353
        base2, mod2 = 239, 1000000007

        prefix1 = [0] * (n + 1)
        prefix2 = [0] * (n + 1)
        power1 = [1] * (n + 1)
        power2 = [1] * (n + 1)

        for i, x in enumerate(nums):
            prefix1[i + 1] = (prefix1[i] * base1 + x) % mod1
            prefix2[i + 1] = (prefix2[i] * base2 + x) % mod2

            power1[i + 1] = power1[i] * base1 % mod1
            power2[i + 1] = power2[i] * base2 % mod2

        def exists_unique(length):
            freq = defaultdict(int)

            for i in range(n - length + 1):
                h1 = (
                    prefix1[i + length]
                    - prefix1[i] * power1[length]
                ) % mod1

                h2 = (
                    prefix2[i + length]
                    - prefix2[i] * power2[length]
                ) % mod2

                freq[(h1, h2)] += 1

            return any(count == 1 for count in freq.values())

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if exists_unique(mid):
                right = mid
            else:
                left = mid + 1

        return left