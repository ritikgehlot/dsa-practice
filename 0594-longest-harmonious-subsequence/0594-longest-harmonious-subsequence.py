class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1

        answer = 0

        for x in count:
            if x + 1 in count:
                answer = max(
                    answer,
                    count[x] + count[x + 1]
                )

        return answer