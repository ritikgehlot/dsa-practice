class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7

        max_value = max(instructions)

        bit = [0] * (max_value + 2)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            result = 0

            while i > 0:
                result += bit[i]
                i -= i & -i

            return result

        answer = 0

        for x in instructions:
            smaller = query(x - 1)
            greater = query(max_value) - query(x)

            answer += min(smaller, greater)
            answer %= MOD

            update(x)

        return answer