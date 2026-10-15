class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        ans = 0

        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] else 0

            sorted_heights = sorted(heights, reverse=True)

            for j, h in enumerate(sorted_heights):
                ans = max(ans, h * (j + 1))

        return ans