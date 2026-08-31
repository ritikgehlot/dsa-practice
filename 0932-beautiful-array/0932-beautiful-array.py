class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        result = [1]

        while len(result) < n:
            odd = [2 * x - 1 for x in result if 2 * x - 1 <= n]
            even = [2 * x for x in result if 2 * x <= n]

            result = odd + even

        return result