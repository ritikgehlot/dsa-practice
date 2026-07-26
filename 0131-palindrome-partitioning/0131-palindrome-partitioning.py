class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPal(x):
            return x == x[::-1]

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                part = s[start:end]
                if isPal(part):
                    path.append(part)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return res