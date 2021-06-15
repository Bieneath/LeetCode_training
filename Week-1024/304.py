# 二维DP问题
from itertools import product
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not any(matrix): 
            self.dp = None
            return
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0] * n for _ in range(m)]
        for i, j in product(range(m), range(n)):
            left = self.dp[i-1][j] if i else 0
            up = self.dp[i][j-1] if j else 0
            up_left = self.dp[i-1][j-1] if i and j else 0
            self.dp[i][j] = up + left - up_left + matrix[i][j]
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.dp: return 0
        left = self.dp[row2][col1-1] if col1 else 0
        up = self.dp[row1-1][col2] if row1 else 0
        up_left = self.dp[row1-1][col1-1] if row1 and col1 else 0
        return self.dp[row2][col2] - left - up + up_left