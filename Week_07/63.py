# 代码一
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        n_rows, n_cols = len(grid), len(grid[0])
        dp = [[0]*n_cols for _ in range(n_rows)]
        dp[0][0] = 1 - grid[0][0]
        for i in range(1, n_rows):
            dp[i][0] = (1 - grid[i][0]) * dp[i-1][0]
        for j in range(1, n_cols):
            dp[0][j] = (1 - grid[0][j]) * dp[0][j-1]
        for i in range(1, n_rows):
            for j in range(1, n_cols):
                dp[i][j] = (1 - grid[i][j]) * (dp[i-1][j] + dp[i][j-1])
        return dp[-1][-1]

# 代码二
# class Solution:
#     def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
#         if not grid or not grid[0]: return 0
#         n_rows, n_cols = len(grid), len(grid[0])
#         dp = [[1]*n_cols for _ in range(n_rows)]
#         for i in range(n_rows):
#             for j in range(n_cols):
#                 if grid[i][j]:
#                     dp[i][j] = 0
#                     continue
#                 if i ==0 and j == 0: continue
#                 if i == 0:
#                     dp[i][j] = dp[i][j-1]
#                 elif j == 0:
#                     dp[i][j] = dp[i-1][j]
#                 else:
#                     dp[i][j] = dp[i-1][j] + dp[i][j-1]
#         return dp[-1][-1]