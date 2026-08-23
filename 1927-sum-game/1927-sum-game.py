class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = right_sum = 0
        left_q = right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # Odd number of '?' means Alice moves last and can always break equality
        if (left_q + right_q) % 2 == 1:
            return True

        # Bob wins only if the digit gap is exactly what the '?' surplus is worth.
        # Multiply by 2 instead of dividing to keep it exact and signed.
        return 2 * (left_sum - right_sum) != 9 * (right_q - left_q)