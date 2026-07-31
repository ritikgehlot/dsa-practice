class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        index = {word: i for i, word in enumerate(words)}
        ans = []

        for i, word in enumerate(words):
            n = len(word)

            for j in range(n + 1):
                left = word[:j]
                right = word[j:]

                # reverse(right) + word
                if left == left[::-1]:
                    rev = right[::-1]

                    if rev in index and index[rev] != i:
                        ans.append([index[rev], i])

                # word + reverse(left)
                # j != n prevents duplicate pairs
                if j != n and right == right[::-1]:
                    rev = left[::-1]

                    if rev in index and index[rev] != i:
                        ans.append([i, index[rev]])

        return ans