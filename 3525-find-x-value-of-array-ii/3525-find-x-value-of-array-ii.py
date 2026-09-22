class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        veltrunigo = queries
        n = len(nums)

        size = 1
        while size < n:
            size <<= 1

        prod = [1] * (2 * size)
        cnt = [[0] * k for _ in range(2 * size)]

        def make_node(i, val):
            val %= k
            prod[i] = val
            cnt[i] = [0] * k
            cnt[i][val] = 1

        def merge(i):
            left = i * 2
            right = left + 1

            p = prod[left]
            prod[i] = (p * prod[right]) % k

            res = cnt[left].copy()

            for r in range(k):
                res[(p * r) % k] += cnt[right][r]

            cnt[i] = res

        for i in range(n):
            make_node(size + i, nums[i])

        for i in range(size - 1, 0, -1):
            merge(i)

        def update(pos, val):
            i = size + pos
            make_node(i, val)

            i >>= 1
            while i:
                merge(i)
                i >>= 1

        def query(l, r):
            l += size
            r += size + 1

            left_nodes = []
            right_nodes = []

            while l < r:
                if l & 1:
                    left_nodes.append(l)
                    l += 1

                if r & 1:
                    r -= 1
                    right_nodes.append(r)

                l >>= 1
                r >>= 1

            nodes = left_nodes + right_nodes[::-1]

            p = 1
            result = [0] * k

            for node in nodes:
                old = result
                result = old.copy()

                for x in range(k):
                    result[(p * x) % k] += cnt[node][x]

                p = (p * prod[node]) % k

            return result

        ans = []

        for index, value, start, x in queries:
            update(index, value)
            ans.append(query(start, n - 1)[x])

        return ans