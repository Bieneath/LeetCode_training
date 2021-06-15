# 这题要求的子串字符是连续的，所以DP转移方程就是if A[i] == B[j]: dp[i][j] = dp[i-1][j-1] + 1
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        ret = 0
        A = ['#'] + A
        B = ['#'] + B
        la, lb = len(A), len(B)
        dp = [[0] * lb for _ in range(la)]
        for i in range(1, la):
            for j in range(1, lb):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ret = max(ret, dp[i][j])
        return ret