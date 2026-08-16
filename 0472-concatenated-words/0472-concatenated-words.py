class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_set = set(words)
        ans = []

        def can_form(word):
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                for j in range(i):
                    if not dp[j]:
                        continue

                    if word[j:i] in words_set:
                        dp[i] = True
                        break

            return dp[n]

        # Process shorter words first
        words.sort(key=len)

        for word in words:
            words_set.remove(word)

            if can_form(word):
                ans.append(word)

            words_set.add(word)

        return ans