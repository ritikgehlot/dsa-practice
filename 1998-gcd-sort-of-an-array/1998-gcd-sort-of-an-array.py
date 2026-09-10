class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        n = len(nums)
        max_num = max(nums)

        parent = list(range(max_num + 1))
        size = [1] * (max_num + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a = find(a)
            b = find(b)

            if a == b:
                return

            if size[a] < size[b]:
                a, b = b, a

            parent[b] = a
            size[a] += size[b]

        # Smallest prime factor
        spf = list(range(max_num + 1))

        for i in range(2, int(max_num ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_num + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # Connect each number with its prime factors
        for x in nums:
            y = x

            while y > 1:
                p = spf[y]
                union(x, p)

                while y % p == 0:
                    y //= p

        # Compare with sorted array
        target = sorted(nums)

        for a, b in zip(nums, target):
            if find(a) != find(b):
                return False

        return True