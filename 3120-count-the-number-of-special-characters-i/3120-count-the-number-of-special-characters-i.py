class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special = set()

        for ch in word:
            if ch.islower() and ch.upper() in word:
                special.add(ch)

        return len(special)