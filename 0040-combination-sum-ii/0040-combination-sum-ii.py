class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, target, path):
            if target == 0:
                res.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, target - candidates[i], path)  # Move to next index
                path.pop()

        dfs(0, target, [])
        return res