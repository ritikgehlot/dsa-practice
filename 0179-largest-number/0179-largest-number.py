from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str, nums))

        def cmp(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0

        strs.sort(key=cmp_to_key(cmp))

        ans = "".join(strs)

        return "0" if ans[0] == "0" else ans