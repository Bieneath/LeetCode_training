class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 构建一个三维DP表，三个维度分别代笔第几天、第几次交易、当前是持有还是未持有股票1代表持有，0代表未持有
        # dp[i][k][1 or 0]即表示在第i天交易了k次情况下持有或者未持有股票的最大利润
        prices = ['#'] + prices
        l = len(prices)
        dp = [[[0] * 2 for _ in range(3)] for _ in range(l)]
        for i in range(0, l):
            for k in range(0, 3):
                # 处理一些初始化问题，continue不能漏！！！
                if i == 0 or k == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = float('-inf')
                    continue
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[-1][-1][0]