class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0
        # (except 0 itself) cannot be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Reverse only half of the number
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # Even digits: x == reversed_half
        # Odd digits: remove middle digit using // 10
        return x == reversed_half or x == reversed_half // 10