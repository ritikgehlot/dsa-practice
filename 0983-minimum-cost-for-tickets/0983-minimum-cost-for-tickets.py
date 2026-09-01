class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel = set(days)
        last = days[-1]

        dp = [0] * (last + 1)

        for day in range(1, last + 1):
            if day not in travel:
                dp[day] = dp[day - 1]
            else:
                one = dp[max(0, day - 1)] + costs[0]
                seven = dp[max(0, day - 7)] + costs[1]
                thirty = dp[max(0, day - 30)] + costs[2]

                dp[day] = min(one, seven, thirty)

        return dp[last]