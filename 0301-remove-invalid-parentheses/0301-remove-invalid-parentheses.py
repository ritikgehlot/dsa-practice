class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = set()

        def dfs(i, left, right, path):
            if i == len(s):
                if left == 0 and right == 0:
                    ans.add(''.join(path))
                return

            if s[i] == '(':
                dfs(i + 1, left, right, path)

                path.append('(')
                dfs(i + 1, left + 1, right, path)
                path.pop()

            elif s[i] == ')':
                dfs(i + 1, left, right, path)

                if left > 0:
                    path.append(')')
                    dfs(i + 1, left - 1, right, path)
                    path.pop()

            else:
                path.append(s[i])
                dfs(i + 1, left, right, path)
                path.pop()

        dfs(0, 0, 0, [])
        
        max_len = max(map(len, ans))
        return [x for x in ans if len(x) == max_len]