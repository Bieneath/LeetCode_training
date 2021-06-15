# 这题思路很奇葩，对我来说难度很高，不但用到了二维DP，而且状态定义也很抽象。建议反复练习、回忆解体思路
# 每片叶子leaves[i]都有三种状态: 0, 1, 2表示左、中、右三种状态，leaves[i][0]可以由leaves[i-1][0]得到，
# leaves[i][1]可以由leaves[i-1][0]与leaves[i-1][1]的min关系得到，leaves[i][2]可以由leaves[i-1][1]和leaves[i-1][2]的min关系得到
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        l = len(leaves)
        dp = [[0, 0, 0] for _ in range(l)]
        dp[0][0] = ('y' == leaves[0])
        # 将几个不符合题目条件的项设置为float('inf')，表示不可能被选中
        dp[0][1] = dp[0][2] = dp[1][2] = float('inf')
        for i in range(1, l):
            isRed = ('r' == leaves[i])
            isYellow = ('y' == leaves[i])
            dp[i][0] = dp[i-1][0] + isYellow # 0这个状态只能从leaves[i-1][0]状态获得
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + isRed # 1这个状态，前面的节点可以是0也可以是1，取两者较小值
            if i > 1: # 第三个及以后的节点才有可能出现状态2
                dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + isYellow # 2这个状态，前面的节点可以是1也可以是2，取两者较小值
        return dp[-1][2]