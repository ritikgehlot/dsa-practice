class Solution:
    def queryString(self, s: str, n: int) -> bool:
        if n > 1000:
            return False

        for x in range(n // 2 + 1, n + 1):
            if bin(x)[2:] not in s:
                return False

        return True