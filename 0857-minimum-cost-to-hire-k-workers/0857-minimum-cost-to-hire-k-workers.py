from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted(
            (w / q, q)
            for q, w in zip(quality, wage)
        )

        max_heap = []
        total_quality = 0
        answer = float("inf")

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q

            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)

            if len(max_heap) == k:
                answer = min(answer, total_quality * ratio)

        return answer