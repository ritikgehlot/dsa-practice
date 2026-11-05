class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])

        heights = [0] * n
        ans = 0

        for i in range(m):

            for j in range(n):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            for right in range(n):
                min_height = float('inf')

                for left in range(right, -1, -1):
                    min_height = min(min_height, heights[left])

                    if min_height == 0:
                        break

                    ans += min_height

        return ans