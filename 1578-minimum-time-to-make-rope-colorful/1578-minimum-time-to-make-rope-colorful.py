class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        total = neededTime[0]
        maximum = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                ans += min(maximum, neededTime[i])
                maximum = max(maximum, neededTime[i])
            else:
                maximum = neededTime[i]

        return ans