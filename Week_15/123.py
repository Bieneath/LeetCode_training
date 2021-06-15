# # 正反二次遍历法
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices: return 0
#         profits = []
#         MIN = float('inf')
#         optimum = 0
#         for p in prices:
#             MIN = min(MIN, p)
#             optimum = max(optimum, p - MIN)
#             profits.append(optimum)
#         MAX = float('-inf')
#         optimum = 0
#         ret = 0
#         for i in range(len(prices)-1, -1, -1):
#             MAX = max(MAX, prices[i])
#             optimum = max(optimum, MAX - prices[i])
#             ret = max(ret, profits[i] + optimum)
#         return ret

# 在二维DP基础上，去掉矩阵，将5个状态用单独的变量表示（计算机中多维列表定位/查找比单独的变量耗时）
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        st00 = 0
        st11 = -prices[0]
        st01 = st10 = st21 = st20 = float('-inf')
        for p in prices[1:]:
            st11 = max(st11, -p)
            st10 = max(st10, st11 + p)
            st21 = max(st21, st10 - p)
            st20 = max(st20, st21 + p)
        return max(st10, st20)

# # 根据股票问题通用解法，第i天的所有状态都可以由i-1天的状态得到，我们可以省略天数这个维度，节省空间
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) < 2: return 0
#         max_k = 2
#         dp = [[0, 0] for _ in range(max_k + 1)]
#         # 初始化第一天的各种情况
#         dp[0][0] = 0
#         dp[1][0] = dp[0][1] = dp[2][0] = dp[2][1] = float('-inf') # 将一些第一天不可能出现的情况设置成-inf
#         dp[1][1] = -prices[0] # 这个表示第一天交易一次持有股票，此时现金数为负第一题的股价
#         for p in prices[1:]:
#             dp[1][1] = max(dp[1][1], -p)
#             dp[1][0] = max(dp[1][0], dp[1][1] + p)
#             dp[2][1] = max(dp[2][1], dp[1][0] - p)
#             dp[2][0] = max(dp[2][0], dp[2][1] + p)
#         return max(dp[1][0], dp[2][0])

# # 股票6题通用解法：https://leetcode-cn.com/circle/article/qiAgHn/
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # dp[i][k][0, 1]，第i天进行了k次购买操作的情况下持有和未持有股票的最大收益
#         prices = ['#'] + prices
#         l = len(prices)
#         max_k = 2
#         dp = [[[0]*2 for _ in range(max_k+1)] for _ in range(l)]
#         for i in range(l):
#             for k in range(max_k+1):
#                 if i == 0 or k == 0:
#                     dp[i][k][0] = 0 # “没有交易->没有持有股票”与“第一天前没有持有股票”都是收益为0的情况。
#                     dp[i][k][1] = float('-inf') # “没有交易持却持有股票”与“第一天前持有股票”都是不能出现的情况！！！
#                     continue
#                 dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
#                 dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
#         return dp[-1][-1][0]