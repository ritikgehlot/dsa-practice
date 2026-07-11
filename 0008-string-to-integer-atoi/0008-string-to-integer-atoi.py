class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        i = 0
        n = len(s)

        # 1. Ignore leading spaces
        while i < n and s[i] == " ":
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i += 1

        # 3. Read digits
        number = 0

        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Check overflow before updating number
            if number > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            number = number * 10 + digit
            i += 1

        return sign * number