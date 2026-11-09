class Solution:
    def maximumGood(self, statements: list[list[int]]) -> int:
        n = len(statements)
        ans = 0

        for mask in range(1 << n):
            good = mask.bit_count()
            valid = True

            for i in range(n):
                if not (mask & (1 << i)):
                    continue

                for j in range(n):
                    statement = statements[i][j]

                    if statement == 2:
                        continue

                    actual = (mask >> j) & 1

                    if actual != statement:
                        valid = False
                        break

                if not valid:
                    break

            if valid:
                ans = max(ans, good)

        return ans