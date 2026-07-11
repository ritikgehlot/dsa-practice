class Solution:
    def longestPalindrome(self, s):
        start = 0
        max_length = 1

        def expand(left, right):
            # Expand while characters are equal
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # Palindrome is from left + 1 to right - 1
            return left + 1, right - 1

        for i in range(len(s)):

            # Odd-length palindrome
            left1, right1 = expand(i, i)
            length1 = right1 - left1 + 1

            if length1 > max_length:
                start = left1
                max_length = length1

            # Even-length palindrome
            left2, right2 = expand(i, i + 1)
            length2 = right2 - left2 + 1

            if length2 > max_length:
                start = left2
                max_length = length2

        return s[start:start + max_length]