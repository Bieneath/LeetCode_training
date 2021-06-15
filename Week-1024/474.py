# 这个又m又n的0-1DP问题，不要列两张DP表！把它们并在一起。先想想只有一个上限的0-1DP问题题解
# dp转移公式是dp[i][j] = max(dp[i-1][j-x] + 1, dp[i-1][j])
# 在这题里有两个参数m和n，因此dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-z][k-o] + 1)，其中z和o为0与1的个数
# 这里有个技巧，因为这里用到了降维，我们必须从最右边往左进行遍历，为了保证j-z和k-o用的还是为改变之前的值！
from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)] # 这里初始化很重要，我们先初始了一个全0的状态！
        for s in strs:
            C = Counter(s)
            z, o = C['0'], C['1']
            for x, y in product(range(m, -1, -1), range(n, -1, -1)): # 技巧点
                if x - z >= 0 and y - o >= 0:
                    dp[x][y] = max(dp[x][y], dp[x-z][y-o] + 1)
        return dp[m][n]