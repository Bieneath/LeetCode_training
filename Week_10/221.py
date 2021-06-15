class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        n_rows, n_cols = len(matrix), len(matrix[0])
        dp = [[0] * n_cols for _ in range(n_rows)]
        ret = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if '1' == matrix[i][j]:
                    dp[i][j] = 1
                    if i * j:
                        dp[i][j] += min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    ret = max(ret, dp[i][j])
        return ret**2