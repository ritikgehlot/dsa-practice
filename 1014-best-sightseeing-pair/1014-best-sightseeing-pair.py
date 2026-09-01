class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best = values[0]
        answer = 0

        for j in range(1, len(values)):
            answer = max(
                answer,
                best + values[j] - j
            )

            best = max(
                best,
                values[j] + j
            )

        return answer