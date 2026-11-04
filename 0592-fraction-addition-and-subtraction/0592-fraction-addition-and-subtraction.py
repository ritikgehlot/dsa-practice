import math
import re

class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = re.findall(r'[+-]?\d+/\d+', expression)

        numerator = 0
        denominator = 1

        for fraction in fractions:
            a, b = map(int, fraction.split('/'))

            numerator = numerator * b + a * denominator
            denominator *= b

            g = math.gcd(abs(numerator), denominator)

            numerator //= g
            denominator //= g

        return f"{numerator}/{denominator}"