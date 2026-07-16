class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"

        for _ in range(2, n + 1):
            temp = ""
            count = 1

            for j in range(1, len(ans) + 1):
                if j < len(ans) and ans[j] == ans[j - 1]:
                    count += 1
                else:
                    temp += str(count) + ans[j - 1]
                    count = 1

            ans = temp

        return ans