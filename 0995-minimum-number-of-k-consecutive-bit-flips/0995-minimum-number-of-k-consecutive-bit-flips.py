class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)

        diff = [0] * (n + 1)
        flip = 0
        ans = 0

        for i in range(n):
            flip ^= diff[i]

            # Current bit is effectively 0
            if nums[i] ^ flip == 0:
                if i + k > n:
                    return -1

                ans += 1
                flip ^= 1
                diff[i + k] ^= 1

        return ans