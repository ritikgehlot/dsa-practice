from collections import Counter

class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums.sort()

        def solve(sums):
            if len(sums) == 1:
                return []

            diff = sums[1] - sums[0]

            cnt = Counter(sums)
            group1 = []
            group2 = []

            for x in sums:
                if cnt[x] > 0:
                    cnt[x] -= 1
                    group1.append(x)

                    cnt[x + diff] -= 1
                    group2.append(x + diff)

            # Zero belongs to group1.
            if 0 in group1:
                return [diff] + solve(group1)

            return [-diff] + solve(group2)

        return solve(sums)