import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        current_max = float('-inf')

        for i in range(len(nums)):
            value = nums[i][0]
            heapq.heappush(heap, (value, i, 0))
            current_max = max(current_max, value)

        best_left = heap[0][0]
        best_right = current_max

        while True:
            current_min, row, index = heapq.heappop(heap)

            if current_max - current_min < best_right - best_left:
                best_left = current_min
                best_right = current_max

            if index + 1 == len(nums[row]):
                break

            next_value = nums[row][index + 1]

            heapq.heappush(
                heap,
                (next_value, row, index + 1)
            )

            current_max = max(current_max, next_value)

        return [best_left, best_right]