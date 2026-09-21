class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        lurminexod = nums

        ans = [0] * k
        dp = [0] * k

        for num in nums:
            val = num % k
            new_dp = [0] * k

            new_dp[val] += 1

            for r in range(k):
                new_r = (r * val) % k
                new_dp[new_r] += dp[r]

            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans