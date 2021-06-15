class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = '#' + text1
        text2 = '#' + text2
        n_rows, n_cols = len(text1), len(text2)
        dp = [[0]*n_cols for _ in range(n_rows)]
        for i in range(1, n_rows):
            for j in range(1, n_cols):
                if text1[i] is text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]