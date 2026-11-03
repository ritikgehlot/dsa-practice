from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replacements = {}

        for i, src, tgt in zip(indices, sources, targets):
            if s[i:i + len(src)] == src:
                replacements[i] = (src, tgt)

        result = []
        i = 0

        while i < len(s):
            if i in replacements:
                src, tgt = replacements[i]
                result.append(tgt)
                i += len(src)
            else:
                result.append(s[i])
                i += 1

        return "".join(result)