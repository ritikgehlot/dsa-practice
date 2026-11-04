from typing import List
from collections import defaultdict
import heapq


class DualHeap:
    def __init__(self):
        self.small = []       # Max heap (negative values)
        self.large = []       # Min heap
        self.delayed = defaultdict(int)

        self.small_size = 0
        self.large_size = 0

        self.small_sum = 0
        self.large_sum = 0

    def prune(self, heap, is_small):
        while heap:
            num = -heap[0] if is_small else heap[0]

            if self.delayed[num] == 0:
                break

            self.delayed[num] -= 1

            if is_small:
                heapq.heappop(heap)
            else:
                heapq.heappop(heap)

    def rebalance(self):
        self.prune(self.small, True)
        self.prune(self.large, False)

        # small can contain at most one extra element.
        while self.small_size > self.large_size + 1:
            num = -heapq.heappop(self.small)

            self.small_sum -= num
            self.large_sum += num

            self.small_size -= 1
            self.large_size += 1

            heapq.heappush(self.large, num)
            self.prune(self.small, True)

        while self.small_size < self.large_size:
            num = heapq.heappop(self.large)

            self.large_sum -= num
            self.small_sum += num

            self.large_size -= 1
            self.small_size += 1

            heapq.heappush(self.small, -num)
            self.prune(self.large, False)

    def add(self, num):
        self.prune(self.small, True)

        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_sum += num
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_sum += num
            self.large_size += 1

        self.rebalance()

    def remove(self, num):
        self.prune(self.small, True)

        self.delayed[num] += 1

        if num <= -self.small[0]:
            self.small_sum -= num
            self.small_size -= 1

            if num == -self.small[0]:
                self.prune(self.small, True)
        else:
            self.large_sum -= num
            self.large_size -= 1

            if self.large and num == self.large[0]:
                self.prune(self.large, False)

        self.rebalance()

    def get_cost(self):
        self.prune(self.small, True)

        median = -self.small[0]

        left_cost = median * self.small_size - self.small_sum
        right_cost = self.large_sum - median * self.large_size

        return left_cost + right_cost


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Step 1: Calculate the minimum cost of every
        # window of size x using its median.
        dh = DualHeap()

        for i in range(x):
            dh.add(nums[i])

        costs = [dh.get_cost()]

        for i in range(x, n):
            dh.remove(nums[i - x])
            dh.add(nums[i])
            costs.append(dh.get_cost())

        # Step 2: Dynamic programming.
        INF = float('inf')

        # prev[i] = minimum cost to select t-1 windows
        # from the first i elements.
        prev = [0] * (n + 1)

        for t in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Option 1: Skip the current element.
                curr[i] = curr[i - 1]

                # Option 2: Select a window ending at i-1.
                if i >= x:
                    start = i - x

                    curr[i] = min(
                        curr[i],
                        prev[start] + costs[start]
                    )

            prev = curr

        return prev[n]