class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        length = n + m - 1

        ans = ['a'] * length
        fixed = [False] * length

        # 1. Apply all T constraints
        for i in range(n):
            if str1[i] != 'T':
                continue

            for j in range(m):
                pos = i + j

                if fixed[pos] and ans[pos] != str2[j]:
                    return ""

                ans[pos] = str2[j]
                fixed[pos] = True

        # 2. Handle all F constraints
        for i in range(n):
            if str1[i] != 'F':
                continue

            # Check whether current substring equals str2
            same = True

            for j in range(m):
                if ans[i + j] != str2[j]:
                    same = False
                    break

            if not same:
                continue

            # Need to break this F substring.
            # Choose the RIGHTMOST unfixed position so that
            # the result remains lexicographically smallest.
            changed = False

            for j in range(i + m - 1, i - 1, -1):
                if not fixed[j]:
                    ans[j] = 'b'
                    fixed[j] = True
                    changed = True
                    break

            if not changed:
                return ""

        return ''.join(ans)