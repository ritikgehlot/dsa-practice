class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        removed = 0
        end = float('-inf')

        for start, finish in intervals:
            if start >= end:
                end = finish
            else:
                removed += 1

        return removed