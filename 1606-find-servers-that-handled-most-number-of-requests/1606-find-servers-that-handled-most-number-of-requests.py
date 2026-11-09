import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        # Fenwick Tree: initially every server is available
        bit = [0] + [i & -i for i in range(1, k + 1)]

        def update(i, delta):
            i += 1
            while i <= k:
                bit[i] += delta
                i += i & -i

        def query(i):
            # Number of available servers from 0 through i
            res = 0
            i += 1
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        def find_kth(target):
            # Find the zero-based index of the target-th available server
            idx = 0
            step = 1 << (k.bit_length() - 1)

            while step:
                nxt = idx + step

                if nxt <= k and bit[nxt] < target:
                    idx = nxt
                    target -= bit[nxt]

                step >>= 1

            return idx

        busy = []
        count = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):

            # Release servers that have finished
            while busy and busy[0][0] <= start:
                finish, server = heapq.heappop(busy)
                update(server, 1)

            # Find the next available server
            total = query(k - 1)
            target = i % k
            before = query(target - 1) if target > 0 else 0

            if total == 0:
                continue

            if total > before:
                server = find_kth(before + 1)
            else:
                server = find_kth(1)

            # Assign the request
            update(server, -1)
            count[server] += 1

            heapq.heappush(busy, (start + duration, server))

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]