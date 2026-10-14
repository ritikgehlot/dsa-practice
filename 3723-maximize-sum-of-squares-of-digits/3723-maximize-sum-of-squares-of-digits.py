class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        digits = [0] * num

        for i in range(num):
            digit = min(9, sum)
            digits[i] = digit
            sum -= digit

        if sum > 0:
            return ""

        return ''.join(map(str, digits))