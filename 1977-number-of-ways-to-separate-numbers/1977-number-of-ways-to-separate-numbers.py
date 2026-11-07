from array import array

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)

        if num[0] == '0':
            return 0

        # LCP preprocessing
        lcp = [array('H', [0]) * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if num[i] == num[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1

        # Prefix DP
        pref = [array('I', [0]) * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for length in range(1, i + 1):
                start = i - length
                ways = 0

                if num[start] != '0':
                    if start == 0:
                        ways = 1
                    else:
                        # Previous number is shorter
                        ways = pref[start][min(length - 1, start)]

                        # Previous number has equal length
                        if start >= length:
                            a = start - length
                            b = start

                            common = lcp[a][b]

                            if (common >= length or
                                num[a + common] <= num[b + common]):

                                ways += (
                                    pref[start][length]
                                    - pref[start][length - 1]
                                )

                    ways %= MOD

                pref[i][length] = (
                    pref[i][length - 1] + ways
                ) % MOD

        return pref[n][n]