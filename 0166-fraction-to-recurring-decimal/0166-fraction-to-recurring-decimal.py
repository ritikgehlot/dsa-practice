class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []

        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        res.append(str(numerator // denominator))
        rem = numerator % denominator

        if rem == 0:
            return "".join(res)

        res.append(".")
        seen = {}

        while rem:
            if rem in seen:
                idx = seen[rem]
                res.insert(idx, "(")
                res.append(")")
                break

            seen[rem] = len(res)
            rem *= 10
            res.append(str(rem // denominator))
            rem %= denominator

        return "".join(res)