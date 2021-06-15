# 股票六连通用算法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = ['#'] + prices # 给prices前面填充一个占位符，方便写代码
        l = len(prices)
        # 构建一个三维DP表，穷举所有可能的状态，三个维度分别代表天数，第几次交易，是否持有股票，1代表持有，2代表未持有
        # dp[i][k][1 or 0]代表第i天已经交易了k次，持有和未持有股票状态下的最大收益
        # 这题由于k这一维的交易次数是固定1次，所以这维可以省略
        dp = [[0] * 2 for _ in range(l)]
        for i in range(l):
            if i == 0: # 处理一些初始化情况
                dp[i][0] = 0 # 在交易开始前未持有股票状态下的收益为0
                dp[i][1] = float('-inf') # 在交易开始前持有股票是一种不可能的状态，这种情况不能被考虑，设置为负无穷是为了匹配之后的max()求值，即负无穷永远不会在max()函数中被返还。
                continue # 初始化完直接进入下次循环
            # 状态转移方程，当状态为dp[i][0]即第i天没有持有股票，导致这种情况的原因是1.第i-1天也没有持有股票dp[i-1][0];2.第i-1天持有股票了，在i天卖了，收益加上当前的股价prices[i]即dp[i-1][1] + prices[i]
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # 当前状态为dp[i][1]即第i天持有股票，导致这种情况的原因是1.第i-1天也持有股票dp[i-1][1];2.第i-1天没持有股票了，在i天买入了，收益减去当前的股价prices[i]即dp[i-1][0] - prices[i]；不过这里比较特殊，因为只允许交易一次，所以买入之前的收益肯定是0。
            dp[i][1] = max(dp[i-1][1], 0 - prices[i])
        return dp[-1][0] # 返回值为dp[-1][0]，因为最后一天将手中股票卖出的收益肯定高于手中还持有股票的收益

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices: return 0
#         l = len(prices)
#         MIN = MAX = 0
#         profit = 0
#         for i in range(1, l):
#             if prices[i] < prices[MIN]:
#                 MIN = i
#                 MAX = i
#             if prices[i] > prices[MAX]:
#                 MAX = i
#             profit = max(profit, prices[MAX] - prices[MIN])
#         return profit