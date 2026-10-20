from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1
        self.length = float('inf')


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()

        for i, word in enumerate(wordsContainer):
            node = root

            if len(word) < node.length:
                node.length = len(word)
                node.index = i

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                if len(word) < node.length:
                    node.length = len(word)
                    node.index = i

        ans = []

        for word in wordsQuery:
            node = root

            for ch in reversed(word):
                if ch not in node.children:
                    break
                node = node.children[ch]

            ans.append(node.index)

        return ans