from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)

        @lru_cache(None)
        def dfs(needs):
            ans = sum(needs[i] * price[i] for i in range(n))

            for offer in special:
                new_needs = []

                for i in range(n):
                    if offer[i] > needs[i]:
                        break
                    new_needs.append(needs[i] - offer[i])
                else:
                    ans = min(
                        ans,
                        offer[-1] + dfs(tuple(new_needs))
                    )

            return ans

        return dfs(tuple(needs))