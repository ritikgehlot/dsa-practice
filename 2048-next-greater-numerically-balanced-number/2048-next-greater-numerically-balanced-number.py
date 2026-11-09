class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        def balanced(num):
            freq = [0] * 10

            for ch in str(num):
                freq[int(ch)] += 1

            for d in range(10):
                if freq[d] != 0 and freq[d] != d:
                    return False

            return True

        candidate = n + 1

        while True:
            if balanced(candidate):
                return candidate

            candidate += 1