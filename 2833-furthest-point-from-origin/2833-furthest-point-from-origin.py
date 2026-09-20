class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        pos = moves.count('R') - moves.count('L')
        wildcards = moves.count('_')
        return abs(pos) + wildcards