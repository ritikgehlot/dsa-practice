class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        odd = -1
        for i in range(26):
            if cnt[i] & 1:
                if odd != -1:
                    return ""
                odd = i

        half = n // 2
        half_cnt = [x // 2 for x in cnt]

        def build(prefix, used):
            suffix = []
            for x in range(26):
                suffix.extend([x] * used[x])
            left_part = prefix + suffix
            result = ''.join(chr(x + 97) for x in left_part)
            if n & 1:
                result += chr(odd + 97)
            result += result[:half][::-1]
            return result

        left = []
        used = half_cnt[:]
        broke = False

        for i in range(half):
            c = ord(target[i]) - 97
            if used[c] == 0:
                broke = True
                break
            used[c] -= 1
            left.append(c)
        else:
            candidate = build(left, used)
            if candidate > target:
                return candidate

        # Try the position where the greedy match first failed,
        # using target[i] itself as the threshold (this was the missing case).
        if broke:
            i = len(left)
            threshold = ord(target[i]) - 97
            for c in range(threshold + 1, 26):
                if used[c] == 0:
                    continue
                used[c] -= 1
                return build(left + [c], used)

        # Backtrack over already-matched positions
        for i in range(len(left) - 1, -1, -1):
            used[left[i]] += 1
            current = left[i]
            for c in range(current + 1, 26):
                if used[c] == 0:
                    continue
                used[c] -= 1
                return build(left[:i] + [c], used)

        return ""