class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        length = len(s)

        def perm(m, k):
            result = 1
            for i in range(k):
                result *= m - i
            return result

        unique = 0

        for digits in range(1, length):
            unique += 9 * perm(9, digits - 1)

        used = set()

        for i in range(length):
            digit = int(s[i])

            start = 1 if i == 0 else 0

            for d in range(start, digit):
                if d not in used:
                    unique += perm(9 - i, length - i - 1)

            if digit in used:
                break

            used.add(digit)

        else:
            unique += 1

        return n - unique