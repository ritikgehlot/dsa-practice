class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target == 0:
            return True

        if x + y < target:
            return False

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        return target % gcd(x, y) == 0