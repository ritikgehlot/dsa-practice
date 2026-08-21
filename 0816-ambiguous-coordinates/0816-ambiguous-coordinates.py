class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]

        def parts(x):
            result = []

            # Integer
            if x == "0" or x[0] != "0":
                result.append(x)

            # Decimal
            if x[-1] != "0":
                for i in range(1, len(x)):
                    left = x[:i]
                    right = x[i:]

                    if left == "0" or left[0] != "0":
                        result.append(left + "." + right)

            return result

        ans = []

        for i in range(1, len(s)):
            left = parts(s[:i])
            right = parts(s[i:])

            for a in left:
                for b in right:
                    ans.append("(" + a + ", " + b + ")")

        return ans