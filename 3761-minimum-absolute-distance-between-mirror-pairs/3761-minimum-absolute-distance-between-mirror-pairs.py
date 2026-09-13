class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        last = {}
        ans = float('inf')

        for j, x in enumerate(nums):
            if x in last:
                ans = min(ans, j - last[x])

            rev = int(str(x)[::-1])
            last[rev] = j

        return -1 if ans == float('inf') else ans