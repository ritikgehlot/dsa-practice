class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []

        for num in arr:
            if not stack or num >= stack[-1]:
                stack.append(num)
            else:
                maximum = stack.pop()

                while stack and stack[-1] > num:
                    stack.pop()

                stack.append(maximum)

        return len(stack)