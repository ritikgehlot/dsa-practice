from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)

        for i, row in enumerate(nums):
            for j, x in enumerate(row):
                diagonals[i + j].append(x)

        ans = []

        for d in range(len(diagonals)):
            ans.extend(reversed(diagonals[d]))

        return ans