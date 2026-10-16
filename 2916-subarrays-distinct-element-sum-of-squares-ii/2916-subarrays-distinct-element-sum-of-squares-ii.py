class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        seg = [0] * (4 * n)
        lazy = [0] * (4 * n)
        seg_sq = [0] * (4 * n)

        def apply(node, l, r, val):
            length = r - l + 1
            seg_sq[node] = (
                seg_sq[node] + 2 * val * seg[node] + length * val * val
            ) % MOD
            seg[node] = (seg[node] + length * val) % MOD
            lazy[node] = (lazy[node] + val) % MOD

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return
            mid = (l + r) // 2
            apply(node * 2, l, mid, lazy[node])
            apply(node * 2 + 1, mid + 1, r, lazy[node])
            lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return
            push(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(node * 2, l, mid, ql, qr, val)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, val)
            seg[node] = (seg[node * 2] + seg[node * 2 + 1]) % MOD
            seg_sq[node] = (seg_sq[node * 2] + seg_sq[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, i, 1)
            last[x] = i
            ans = (ans + seg_sq[1]) % MOD

        return ans