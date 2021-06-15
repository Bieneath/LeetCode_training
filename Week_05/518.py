class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins = ['#'] + coins # add a dummy item in the begin of coins list
        # 初始化DP表
        dp = [[0] * (amount+1) for _ in range(len(coins))]
        for _ in range(len(coins)): dp[_][0] = 1
        
        for i in range(1, len(coins)):
            n = coins[i]
            for j in range(1, amount+1):
                use_coin = 0 if j-n < 0 else dp[i][j-n]
                not_use_coin = dp[i-1][j]
                dp[i][j] = use_coin + not_use_coin
        return dp[-1][-1]

# 递归方法（超时）
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         coins.sort()
#         global ret
#         ret = 0
#         def dfs(path, cur_amount):
#             if cur_amount < 0: 
#                 return
#             if cur_amount == 0:
#                 global ret
#                 ret += 1
#                 return
#             for c in coins:
#                 if not path or c >= path[-1]:
#                     dfs(path + [c], cur_amount - c)
#         dfs([], amount)
#         return ret