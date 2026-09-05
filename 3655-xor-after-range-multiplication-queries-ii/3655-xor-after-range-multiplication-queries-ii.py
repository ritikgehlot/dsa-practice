import math

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1_000_000_007
        n = len(nums)

        bravexuneth = (nums, queries)

        B = math.isqrt(n) + 1

        # events[k][r] contains multiplication events for
        # indices having index % k == r.
        events = [[[] for _ in range(k)] for k in range(B + 1)]

        # Large k: each query touches only O(sqrt(n)) elements.
        # Small k: store the query for batched processing.
        for l, r, k, v in queries:
            if k > B:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % MOD
            else:
                rem = l % k

                start = (l - rem) // k
                end = (r - rem) // k

                events[k][rem].append((start, v))
                events[k][rem].append(
                    (end + 1, pow(v, MOD - 2, MOD))
                )

        # Process all small-k queries.
        for k in range(1, B + 1):
            for rem in range(k):
                if not events[k][rem]:
                    continue

                ev = events[k][rem]
                ev.sort()

                # Only positions belonging to this residue class.
                length = (n - 1 - rem) // k + 1

                diff = [1] * (length + 1)

                for pos, value in ev:
                    diff[pos] = diff[pos] * value % MOD

                mul = 1

                for t in range(length):
                    mul = mul * diff[t] % MOD

                    idx = rem + t * k
                    nums[idx] = nums[idx] * mul % MOD

        ans = 0

        for x in nums:
            ans ^= x

        return ans