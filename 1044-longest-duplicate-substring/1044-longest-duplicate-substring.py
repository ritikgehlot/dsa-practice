class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)

        sa = list(range(n))
        rank = [ord(c) for c in s]
        tmp = [0] * n
        k = 1

        while k < n:
            sa.sort(key=lambda i: (
                rank[i],
                rank[i + k] if i + k < n else -1
            ))

            tmp[sa[0]] = 0

            for i in range(1, n):
                a = sa[i - 1]
                b = sa[i]

                prev = (
                    rank[a],
                    rank[a + k] if a + k < n else -1
                )

                curr = (
                    rank[b],
                    rank[b + k] if b + k < n else -1
                )

                tmp[b] = tmp[a] + (prev != curr)

            rank, tmp = tmp, rank

            if rank[sa[-1]] == n - 1:
                break

            k *= 2

        lcp = [0] * n
        pos = [0] * n

        for i in range(n):
            pos[sa[i]] = i

        h = 0
        best = 0
        start = 0

        for i in range(n):
            r = pos[i]

            if r == 0:
                continue

            j = sa[r - 1]

            while (
                i + h < n
                and j + h < n
                and s[i + h] == s[j + h]
            ):
                h += 1

            lcp[r] = h

            if h > best:
                best = h
                start = i

            if h:
                h -= 1

        return s[start:start + best]