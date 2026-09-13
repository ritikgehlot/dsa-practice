from collections import Counter

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        a = []
        b = []
        n = len(img1)

        for i in range(n):
            for j in range(n):
                if img1[i][j]:
                    a.append((i, j))
                if img2[i][j]:
                    b.append((i, j))

        count = Counter()

        for x1, y1 in a:
            for x2, y2 in b:
                count[(x2 - x1, y2 - y1)] += 1

        return max(count.values(), default=0)