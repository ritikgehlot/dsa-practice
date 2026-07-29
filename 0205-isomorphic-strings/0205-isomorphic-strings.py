class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp1 = {}
        mp2 = {}

        for a, b in zip(s, t):
            if (a in mp1 and mp1[a] != b) or (b in mp2 and mp2[b] != a):
                return False

            mp1[a] = b
            mp2[b] = a

        return True