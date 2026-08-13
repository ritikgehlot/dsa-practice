class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        last = stones[-1]

        memo = {}

        def dfs(pos, jump):
            if pos == last:
                return True

            if (pos, jump) in memo:
                return memo[(pos, jump)]

            for step in (jump - 1, jump, jump + 1):
                if step > 0 and pos + step in stone_set:
                    if dfs(pos + step, step):
                        memo[(pos, jump)] = True
                        return True

            memo[(pos, jump)] = False
            return False

        return dfs(0, 0)