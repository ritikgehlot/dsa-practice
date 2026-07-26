from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, step = q.popleft()

            if word == endWord:
                return step

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nxt = word[:i] + c + word[i + 1:]
                    if nxt in wordSet:
                        wordSet.remove(nxt)
                        q.append((nxt, step + 1))

        return 0