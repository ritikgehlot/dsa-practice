from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        chars = sorted(c for c in freq if freq[c] >= k)  # ascending

        def valid(candidate):
            matched = index = 0
            for ch in s:
                if ch == candidate[index]:
                    index += 1
                    if index == len(candidate):
                        matched += 1
                        index = 0
                        if matched == k:
                            return True
            return False

        queue = deque([""])
        ans = ""
        while queue:
            curr = queue.popleft()
            for ch in chars:
                candidate = curr + ch
                if valid(candidate):
                    ans = candidate
                    queue.append(candidate)
        return ans