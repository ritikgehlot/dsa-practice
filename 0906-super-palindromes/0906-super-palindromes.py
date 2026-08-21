class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:

        L = int(left)
        R = int(right)

        def isPalindrome(n):
            s = str(n)
            return s == s[::-1]

        ans = 0

        # Generate palindromes from their first half.
        # sqrt(10^18) = 10^9, so we only need roots <= 10^9.

        for x in range(1, 100000):
            s = str(x)

            # Odd-length palindrome
            p = int(s + s[-2::-1])

            if p * p > R:
                break

            if p * p >= L and isPalindrome(p * p):
                ans += 1

            # Even-length palindrome
            p = int(s + s[::-1])

            if p * p >= L and p * p <= R and isPalindrome(p * p):
                ans += 1

        return ans