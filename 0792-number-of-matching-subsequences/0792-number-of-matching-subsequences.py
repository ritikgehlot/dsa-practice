from collections import defaultdict, deque

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(deque)

        for word in words:
            waiting[word[0]].append((word, 0))

        ans = 0

        for ch in s:
            q = waiting[ch]
            size = len(q)

            for _ in range(size):
                word, i = q.popleft()
                i += 1

                if i == len(word):
                    ans += 1
                else:
                    waiting[word[i]].append((word, i))

        return ans