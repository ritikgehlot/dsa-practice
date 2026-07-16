class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, target, path):
            if target == 0:
                res.append(path[:])
                return

            if index == len(candidates) or target < 0:
                return

            # Take current number
            path.append(candidates[index])
            dfs(index, target - candidates[index], path)
            path.pop()

            # Skip current number
            dfs(index + 1, target, path)

        dfs(0, target, [])
        return res