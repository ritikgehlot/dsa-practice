class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)

        high = max(
            stones[-1] - stones[1],
            stones[-2] - stones[0]
        ) - (n - 2)

        low = n

        j = 0

        for i in range(n):
            while j + 1 < n and stones[j + 1] - stones[i] + 1 <= n:
                j += 1

            count = j - i + 1

            if count == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                low = min(low, 2)
            else:
                low = min(low, n - count)

        return [low, high]