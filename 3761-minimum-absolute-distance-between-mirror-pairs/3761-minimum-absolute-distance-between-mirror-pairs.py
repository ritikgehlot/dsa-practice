class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        pos = {}
        ans = float('inf')

        for i, x in enumerate(nums):
            if x in pos:
                ans = min(ans, i - pos[x])

            rev = int(str(x)[::-1])
            pos[rev] = i

        return -1 if ans == float('inf') else ans