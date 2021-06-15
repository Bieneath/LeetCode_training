# 基于博弈论的动态规划
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l = len(piles)
        dp = [[-1] * l for _ in range(l)]
        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            if i >= j:
                dp[i][j] = piles[i]
            else:
                dp[i][j] = sum(piles[i:j+1]) - min(dfs(i+1, j), dfs(i, j-1))
            return dp[i][j]
        dfs(0, l-1)
        return 2 * dp[0][l-1] > sum(piles)