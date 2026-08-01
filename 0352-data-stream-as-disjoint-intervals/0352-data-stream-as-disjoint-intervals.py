class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        if not self.nums:
            return []

        arr = sorted(self.nums)
        ans = []

        start = end = arr[0]

        for num in arr[1:]:
            if num == end + 1:
                end = num
            else:
                ans.append([start, end])
                start = end = num

        ans.append([start, end])
        return ans