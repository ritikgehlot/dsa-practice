from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(None)
        def solve(i: int, j: int) -> bool:
            # Pattern finish ho gaya
            if j == len(p):
                return i == len(s)

            # Current character match karta hai ya nahi
            first_match = (
                i < len(s)
                and (s[i] == p[j] or p[j] == '.')
            )

            # Check whether next pattern character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                return (
                    solve(i, j + 2)              # Zero occurrences
                    or
                    (first_match and solve(i + 1, j))  # One or more
                )

            # Normal character or '.'
            return first_match and solve(i + 1, j + 1)

        return solve(0, 0)