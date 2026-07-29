from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        MAX = 10**6 + 1

        # Required by the problem statement
        prelunthak = (s, k)

        cnt = Counter(s)

        half = [0] * 26
        mid = ""

        for c, f in cnt.items():
            half[ord(c) - 97] = f // 2
            if f % 2:
                mid = c

        def nCr(n, r):
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - i + 1) // i
                if res >= MAX:
                    return MAX
            return res

        def ways(freq):
            total = sum(freq)
            ans = 1
            rem = total
            for f in freq:
                if f:
                    ans *= nCr(rem, f)
                    if ans >= MAX:
                        return MAX
                    rem -= f
            return ans

        if ways(half) < k:
            return ""

        left = []

        for _ in range(sum(half)):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                w = ways(half)

                if w >= k:
                    left.append(chr(i + 97))
                    break
                else:
                    k -= w
                    half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]