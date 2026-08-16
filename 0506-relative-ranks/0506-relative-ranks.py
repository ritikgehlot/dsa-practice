class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)

        order = sorted(
            range(n),
            key=lambda i: score[i],
            reverse=True
        )

        ans = [""] * n

        for rank, index in enumerate(order):
            if rank == 0:
                ans[index] = "Gold Medal"
            elif rank == 1:
                ans[index] = "Silver Medal"
            elif rank == 2:
                ans[index] = "Bronze Medal"
            else:
                ans[index] = str(rank + 1)

        return ans