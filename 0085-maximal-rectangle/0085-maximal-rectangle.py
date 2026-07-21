class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        n = len(matrix[0])
        heights = [0] * n
        ans = 0

        def largestRectangle(heights):
            stack = []
            res = 0
            arr = heights + [0]

            for i, h in enumerate(arr):
                while stack and arr[stack[-1]] > h:
                    height = arr[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    res = max(res, height * width)
                stack.append(i)

            return res

        for row in matrix:
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0
            ans = max(ans, largestRectangle(heights))

        return ans