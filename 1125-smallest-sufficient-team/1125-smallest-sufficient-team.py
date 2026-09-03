class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill = {s: i for i, s in enumerate(req_skills)}
        full = (1 << len(req_skills)) - 1

        masks = []
        for p in people:
            mask = 0
            for s in p:
                if s in skill:
                    mask |= 1 << skill[s]
            masks.append(mask)

        dp = {0: []}

        for i, mask in enumerate(masks):
            for state, team in list(dp.items()):
                new_state = state | mask

                if new_state not in dp or len(dp[new_state]) > len(team) + 1:
                    dp[new_state] = team + [i]

        return dp[full]