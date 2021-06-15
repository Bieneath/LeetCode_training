# 股票六连通用算法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = ['#'] + prices
        l = len(prices)
        dp = [[0] * 2 for _ in range(l)]
        for i in range(l):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = float('-inf')
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[-1][0]

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l = len(prices)
#         dp = [0] * l
#         for i in range(1, l):
#             dp[i] = max(dp[i-1], dp[i-1] + prices[i] - prices[i-1])
#         return dp[-1]