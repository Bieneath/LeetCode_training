# 比较简单的DP问题
import copy
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        n_rows, n_cols = len(grid), len(grid[0])
        dp = copy.deepcopy(grid) # 可以在原grid上操作，省去deepcopy的时间
        for i in range(n_rows):
            for j in range(n_cols):
                if i == j == 0: continue
                up = dp[i-1][j] if i>0 else float('inf')
                left = dp[i][j-1] if j>0 else float('inf')
                dp[i][j] = min(up, left) + grid[i][j]
        return dp[-1][-1]