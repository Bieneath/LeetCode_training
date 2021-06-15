class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = ['#'] + prices
        l = len(prices)
        dp = [[0] * 2 for _ in range(l)]
        for i in range(l):
            if i == 0:
                dp[i][1] = float('-inf')
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            if i == 1: # 第一天买入只要考虑当天股价就行
                dp[i][1] = -prices[i]
            else: # 因为有冻结期，在i-2天卖出股票的最大收益和到i-1天时相同（不能进行任何买卖），所以直接用dp[i-2][0]的结果扣掉prices[i]的股价。
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        return dp[-1][0]