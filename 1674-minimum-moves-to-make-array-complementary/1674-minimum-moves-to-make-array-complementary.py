class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = 2
            high = 2 * limit

            diff[low] += 2
            diff[high + 1] -= 2

            one_move_low = min(a, b) + 1
            one_move_high = max(a, b) + limit

            diff[one_move_low] -= 1
            diff[one_move_high + 1] += 1

            target = a + b
            diff[target] -= 1
            diff[target + 1] += 1

        ans = n
        moves = 0

        for target in range(2, 2 * limit + 1):
            moves += diff[target]
            ans = min(ans, moves)

        return ans