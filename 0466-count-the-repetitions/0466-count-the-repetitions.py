class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not set(s2).issubset(set(s1)):
            return 0

        pos = 0
        count = 0
        seen = {}

        k = 0

        while k < n1:
            for ch in s1:
                if ch == s2[pos]:
                    pos += 1
                    if pos == len(s2):
                        pos = 0
                        count += 1

            k += 1

            if pos in seen:
                old_k, old_count = seen[pos]

                cycle_len = k - old_k
                cycle_count = count - old_count

                remaining = n1 - k
                times = remaining // cycle_len

                k += times * cycle_len
                count += times * cycle_count
            else:
                seen[pos] = (k, count)

        return count // n2