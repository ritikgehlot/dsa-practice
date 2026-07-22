class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total = s.count('1')

        # blocks: (char, start, end) inclusive
        blocks = []
        i = 0
        while i < n:
            j = i
            while j + 1 < n and s[j + 1] == s[i]:
                j += 1
            blocks.append((s[i], i, j))
            i = j + 1

        bid = [0] * n
        for k, (_, a, b) in enumerate(blocks):
            for p in range(a, b + 1):
                bid[p] = k

        m = len(blocks)

        # unclipped gain for a '1'-block at k flanked by zero-runs
        gain = [0] * m
        for k in range(1, m - 1):
            if blocks[k][0] == '1':
                gain[k] = (blocks[k-1][2] - blocks[k-1][1] + 1) + \
                          (blocks[k+1][2] - blocks[k+1][1] + 1)

        sp = [gain[:]]
        p = 1
        while (1 << p) <= m:
            prev, half = sp[-1], 1 << (p - 1)
            sp.append([max(prev[x], prev[x + half]) for x in range(m - (1 << p) + 1)])
            p += 1

        def qmax(lo, hi):
            if lo > hi or lo < 0 or hi >= m:
                return 0
            k = (hi - lo + 1).bit_length() - 1
            return max(sp[k][lo], sp[k][hi - (1 << k) + 1])

        res = []
        for l, r in queries:
            bl, br = bid[l], bid[r]
            best = qmax(bl + 2, br - 2)          # fully-interior triples

            for k in (bl, bl + 1, br - 1, br):   # boundary triples need clipping
                if not (0 < k < m - 1) or blocks[k][0] != '1':
                    continue
                if blocks[k][1] < l or blocks[k][2] > r:
                    continue
                a = min(blocks[k-1][2], r) - max(blocks[k-1][1], l) + 1
                b = min(blocks[k+1][2], r) - max(blocks[k+1][1], l) + 1
                if a > 0 and b > 0:
                    best = max(best, a + b)

            res.append(total + best)
        return res