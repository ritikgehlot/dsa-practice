from functools import lru_cache

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Factorize t into prime factors 2, 3, 5, 7
        temp_t = t
        counts = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                counts[p] += 1
                temp_t //= p

        # If t has prime factors other than 2, 3, 5, 7, it's impossible.
        if temp_t > 1:
            return "-1"

        def get_factors(d):
            """Returns prime factor counts (2, 3, 5, 7) for a digit d."""
            f = {2: 0, 3: 0, 5: 0, 7: 0}
            if d in (2, 4, 8):
                if d == 2: f[2] = 1
                elif d == 4: f[2] = 2
                elif d == 8: f[2] = 3
            elif d in (3, 9):
                if d == 3: f[3] = 1
                elif d == 9: f[3] = 2
            elif d == 6:
                f[2], f[3] = 1, 1
            elif d == 5:
                f[5] = 1
            elif d == 7:
                f[7] = 1
            return f

        @lru_cache(None)
        def min_23(r2, r3):
            """Minimum digits needed to satisfy required factors of 2 and 3."""
            if r2 <= 0 and r3 <= 0:
                return 0
            res = float("inf")
            # Try digits containing factor 3: 9, 6, 3
            if r3 > 0:
                res = min(res, 1 + min_23(r2, r3 - 2))      # digit 9
                res = min(res, 1 + min_23(r2 - 1, r3 - 1))  # digit 6
                res = min(res, 1 + min_23(r2, r3 - 1))      # digit 3
            # Try digits containing factor 2: 8, 4, 2
            if r2 > 0:
                res = min(res, 1 + min_23(r2 - 3, r3))      # digit 8
                res = min(res, 1 + min_23(r2 - 2, r3))      # digit 4
                res = min(res, 1 + min_23(r2 - 1, r3))      # digit 2
            return res

        def min_digits_needed(r2, r3, r5, r7):
            """Minimum total digits needed to satisfy all required factors."""
            return max(0, r5) + max(0, r7) + min_23(max(0, r2), max(0, r3))

        def fill_suffix(length, r2, r3, r5, r7):
            """Fills a suffix of given length greedily with smallest possible digits."""
            if min_digits_needed(r2, r3, r5, r7) > length:
                return None

            res = []
            curr = [max(0, r2), max(0, r3), max(0, r5), max(0, r7)]

            for rem_len in range(length, 0, -1):
                for d in range(1, 10):
                    f = get_factors(d)
                    next_reqs = [
                        max(0, curr[0] - f[2]),
                        max(0, curr[1] - f[3]),
                        max(0, curr[2] - f[5]),
                        max(0, curr[3] - f[7]),
                    ]
                    if min_digits_needed(*next_reqs) <= rem_len - 1:
                        res.append(str(d))
                        curr = next_reqs
                        break
            return "".join(res)

        n = len(num)
        first_zero = num.find("0")
        limit = first_zero if first_zero != -1 else n

        # Calculate factor requirements after processing valid prefix digits
        prefix_reqs = []
        cur = [counts[2], counts[3], counts[5], counts[7]]
        prefix_reqs.append(list(cur))

        for i in range(limit):
            d = int(num[i])
            f = get_factors(d)
            cur[0] = max(0, cur[0] - f[2])
            cur[1] = max(0, cur[1] - f[3])
            cur[2] = max(0, cur[2] - f[5])
            cur[3] = max(0, cur[3] - f[7])
            prefix_reqs.append(list(cur))

        # Check if num itself works (no zeros and all factors satisfied)
        if first_zero == -1 and min_digits_needed(*cur) == 0:
            return num

        # Try matching prefix of length i
        start_i = limit if first_zero != -1 else n - 1
        for i in range(start_i, -1, -1):
            r2, r3, r5, r7 = prefix_reqs[i]
            # If num[i] is '0', replacing it with any digit 1..9 makes the result larger
            start_d = 1 if (i < n and num[i] == "0") else int(num[i]) + 1

            for d in range(start_d, 10):
                f = get_factors(d)
                nr2 = max(0, r2 - f[2])
                nr3 = max(0, r3 - f[3])
                nr5 = max(0, r5 - f[5])
                nr7 = max(0, r7 - f[7])

                suf = fill_suffix(n - 1 - i, nr2, nr3, nr5, nr7)
                if suf is not None:
                    return num[:i] + str(d) + suf

        # If no number of length n exists, construct the smallest of length max(n + 1, min_digits_needed)
        req_len = max(n + 1, min_digits_needed(counts[2], counts[3], counts[5], counts[7]))
        return fill_suffix(req_len, counts[2], counts[3], counts[5], counts[7])