from math import comb

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        v, h = destination
        ans = []

        while h > 0 or v > 0:
            if h == 0:
                ans.append('V')
                v -= 1
            elif v == 0:
                ans.append('H')
                h -= 1
            else:
                count = comb(h + v - 1, v)

                if k <= count:
                    ans.append('H')
                    h -= 1
                else:
                    ans.append('V')
                    k -= count
                    v -= 1

        return ''.join(ans)