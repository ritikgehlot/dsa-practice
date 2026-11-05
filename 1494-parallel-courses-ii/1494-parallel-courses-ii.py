class Solution:
    def minNumberOfSemesters(
        self, n: int, relations: list[list[int]], k: int
    ) -> int:

        prereq = [0] * n

        for prev, nxt in relations:
            prereq[nxt - 1] |= 1 << (prev - 1)

        total = 1 << n
        dp = [float('inf')] * total
        dp[0] = 0

        for mask in range(total):
            if dp[mask] == float('inf'):
                continue

            available = 0

            for i in range(n):
                bit = 1 << i

                if not (mask & bit) and (mask & prereq[i]) == prereq[i]:
                    available |= bit

            # Enumerate every non-empty subset of available courses.
            sub = available

            while sub:
                if sub.bit_count() <= k:
                    new_mask = mask | sub
                    dp[new_mask] = min(
                        dp[new_mask],
                        dp[mask] + 1
                    )

                sub = (sub - 1) & available

        return dp[-1]