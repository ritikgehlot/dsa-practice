class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)

        overlap = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                max_overlap = min(
                    len(words[i]),
                    len(words[j])
                )

                for k in range(max_overlap, 0, -1):
                    if words[i][-k:] == words[j][:k]:
                        overlap[i][j] = k
                        break

        dp = [[""] * n for _ in range(1 << n)]

        for i in range(n):
            dp[1 << i][i] = words[i]

        for mask in range(1 << n):
            for last in range(n):

                if not (mask & (1 << last)):
                    continue

                if not dp[mask][last]:
                    continue

                for nxt in range(n):

                    if mask & (1 << nxt):
                        continue

                    new_mask = mask | (1 << nxt)

                    candidate = (
                        dp[mask][last]
                        + words[nxt][overlap[last][nxt]:]
                    )

                    if (
                        not dp[new_mask][nxt]
                        or len(candidate) < len(dp[new_mask][nxt])
                        or (
                            len(candidate) == len(dp[new_mask][nxt])
                            and candidate < dp[new_mask][nxt]
                        )
                    ):
                        dp[new_mask][nxt] = candidate

        full = (1 << n) - 1

        answer = ""

        for i in range(n):
            if not answer or len(dp[full][i]) < len(answer):
                answer = dp[full][i]
            elif (
                len(dp[full][i]) == len(answer)
                and dp[full][i] < answer
            ):
                answer = dp[full][i]

        return answer