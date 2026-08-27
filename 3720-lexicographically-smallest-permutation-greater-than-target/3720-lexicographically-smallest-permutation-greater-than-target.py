class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        n = len(s)

        def build(pos, greater):
            if pos == n:
                return "" if greater else None

            t = ord(target[pos]) - ord('a')

            # If already greater, simply use the smallest
            # remaining character at every position.
            if greater:
                for c in range(26):
                    if cnt[c]:
                        cnt[c] -= 1
                        suffix = build(pos + 1, True)
                        cnt[c] += 1

                        if suffix is not None:
                            return chr(c + ord('a')) + suffix

                return None

            # First try equal to target[pos].
            if cnt[t]:
                cnt[t] -= 1

                suffix = build(pos + 1, False)

                cnt[t] += 1

                if suffix is not None:
                    return chr(t + ord('a')) + suffix

            # If equality is impossible, try the smallest
            # character strictly greater than target[pos].
            for c in range(t + 1, 26):
                if cnt[c]:
                    cnt[c] -= 1

                    # Once greater, remaining characters are
                    # simply sorted.
                    result = chr(c + ord('a'))

                    for x in range(26):
                        if cnt[x]:
                            result += chr(x + ord('a')) * cnt[x]

                    cnt[c] += 1

                    return result

            return None

        result = build(0, False)

        return result if result is not None else ""