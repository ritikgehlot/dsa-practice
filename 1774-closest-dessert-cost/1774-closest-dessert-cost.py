class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        best = baseCosts[0]

        def dfs(i, total):
            nonlocal best

            if abs(total - target) < abs(best - target) or (
                abs(total - target) == abs(best - target) and total < best
            ):
                best = total

            if i == len(toppingCosts):
                return

            if total > target and total - target > abs(best - target):
                return

            dfs(i + 1, total)
            dfs(i + 1, total + toppingCosts[i])
            dfs(i + 1, total + 2 * toppingCosts[i])

        for base in baseCosts:
            dfs(0, base)

        return best