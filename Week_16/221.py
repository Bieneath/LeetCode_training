# dp[i][j]只和上、下、左上相关联，原本需要三个值分别表示这3个方向的'1'的长度，不过仔细分析之后就能得出因为是求最大正方形，所以上下左上的'1'个数必须相等，因此只要记录三个方向的最小值即可。
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