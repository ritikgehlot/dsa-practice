from functools import lru_cache

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:

        sticker_counts = []

        for sticker in stickers:
            count = [0] * 26

            for ch in sticker:
                count[ord(ch) - ord('a')] += 1

            sticker_counts.append(count)

        @lru_cache(None)
        def dfs(remain):
            if not remain:
                return 0

            target_count = [0] * 26

            for ch in remain:
                target_count[ord(ch) - ord('a')] += 1

            ans = float('inf')

            # Try every sticker
            for sticker in sticker_counts:

                # Optimization:
                # sticker must contain the first remaining character
                first = ord(remain[0]) - ord('a')

                if sticker[first] == 0:
                    continue

                new_remain = []

                used = [0] * 26

                for i in range(26):
                    used[i] = max(
                        0,
                        target_count[i] - sticker[i]
                    )

                for i in range(26):
                    new_remain.extend(
                        chr(i + ord('a')) * used[i]
                    )

                new_remain = ''.join(new_remain)

                result = dfs(new_remain)

                if result != float('inf'):
                    ans = min(ans, 1 + result)

            return ans

        result = dfs(target)

        return -1 if result == float('inf') else result