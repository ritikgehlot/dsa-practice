class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)

        if n == 1:
            return 1

        up = 1
        down = 1
        answer = 1

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up = down + 1
                down = 1
            elif arr[i] < arr[i - 1]:
                down = up + 1
                up = 1
            else:
                up = 1
                down = 1

            answer = max(answer, up, down)

        return answer