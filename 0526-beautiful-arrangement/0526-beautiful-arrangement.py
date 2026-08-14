class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(pos, mask):
            if pos > n:
                return 1

            total = 0

            for num in range(1, n + 1):
                bit = 1 << (num - 1)

                if mask & bit:
                    continue

                if num % pos == 0 or pos % num == 0:
                    total += backtrack(pos + 1, mask | bit)

            return total

        return backtrack(1, 0)