class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:

        s = str(n)
        length = len(s)
        d = len(digits)

        ans = 0

        # Numbers with fewer digits
        for l in range(1, length):
            ans += d ** l

        # Numbers with the same number of digits
        for i in range(length):

            smaller = 0

            for digit in digits:
                if digit < s[i]:
                    smaller += 1

            ans += smaller * (d ** (length - i - 1))

            if s[i] not in digits:
                return ans

        # n itself is possible
        return ans + 1