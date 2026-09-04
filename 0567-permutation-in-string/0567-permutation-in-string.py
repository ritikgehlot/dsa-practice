class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26

        for ch in s1:
            need[ord(ch) - 97] += 1

        k = len(s1)

        for i in range(len(s2)):
            window[ord(s2[i]) - 97] += 1

            if i >= k:
                window[ord(s2[i - k]) - 97] -= 1

            if window == need:
                return True

        return False