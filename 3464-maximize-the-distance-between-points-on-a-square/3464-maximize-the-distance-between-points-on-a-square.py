from bisect import bisect_left

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        perimeter = 4 * side
        nums = []

        for x, y in points:
            if x == 0:
                nums.append(y)
            elif y == side:
                nums.append(side + x)
            elif x == side:
                nums.append(3 * side - y)
            else:
                nums.append(4 * side - x)

        nums.sort()
        n = len(nums)
        ext = nums + [x + perimeter for x in nums]

        def can(d):
            for start in range(n):
                cur = start
                limit = ext[start] + perimeter - d
                valid = True

                for _ in range(k - 1):
                    nxt = bisect_left(ext, ext[cur] + d, cur + 1)

                    if nxt >= start + n or ext[nxt] > limit:
                        valid = False
                        break

                    cur = nxt

                if valid:
                    return True

            return False

        left, right = 0, side

        while left < right:
            mid = (left + right + 1) // 2

            if can(mid):
                left = mid
            else:
                right = mid - 1

        return left