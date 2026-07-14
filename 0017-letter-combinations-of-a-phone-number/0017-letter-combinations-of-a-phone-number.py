from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        answer = []

        def backtrack(index: int, current: str) -> None:
            # All digits have been processed
            if index == len(digits):
                answer.append(current)
                return

            # Try every letter mapped to the current digit
            for letter in phone[digits[index]]:
                backtrack(index + 1, current + letter)

        backtrack(0, "")
        return answer