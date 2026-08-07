from math import gcd

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        g = nums[0]

        for num in nums[1:]:
            g = gcd(g, num)

        return g == 1