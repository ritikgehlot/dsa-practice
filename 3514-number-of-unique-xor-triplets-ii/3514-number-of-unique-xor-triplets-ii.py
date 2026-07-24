class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        vals = set(nums)

        pair_xor = set()
        for x in vals:
            for y in vals:
                pair_xor.add(x ^ y)

        ans = set()
        for p in pair_xor:
            for x in vals:
                ans.add(p ^ x)

        return len(ans)