class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teams = sorted(votes[0])
        count = {x: [0] * len(teams) for x in teams}

        for vote in votes:
            for i, team in enumerate(vote):
                count[team][i] += 1

        teams.sort(key=lambda x: (count[x], -ord(x)), reverse=True)

        return ''.join(teams)