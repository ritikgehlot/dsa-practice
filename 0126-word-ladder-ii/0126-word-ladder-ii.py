from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = {beginWord}
        found = False

        while level and not found:
            nextLevel = defaultdict(list)

            # Remove current level words
            wordSet -= level

            for word in level:
                word = list(word)

                for i in range(len(word)):
                    old = word[i]

                    for c in "abcdefghijklmnopqrstuvwxyz":
                        word[i] = c
                        nxt = "".join(word)

                        if nxt in wordSet:
                            nextLevel[nxt].append("".join(word[:i] + [old] + word[i+1:]))

                    word[i] = old

            level = set(nextLevel.keys())

            for child, pars in nextLevel.items():
                parents[child].extend(pars)

            if endWord in level:
                found = True

        if not found:
            return []

        ans = []

        def dfs(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return

            for p in parents[word]:
                dfs(p, path + [p])

        dfs(endWord, [endWord])
        return ans