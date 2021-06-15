class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        l = len(nums)
        dp = [[-1] * l for _ in range(l)]
        # print(dp[1][1])
        # 基于博弈论的递归求法；
        # dp[le][ri]的意义为在[le, ri]这段数字中先手能获得的最大分数
        def dfs(le, ri): # 整个dfs的作用就是填写dp表
            if dp[le][ri] != -1: return dp[le][ri]
            # 当le==ri时候，即剩余数字只剩下一个，那么就取这个数字
            if le >= ri: 
                dp[le][ri] = nums[le]
            else: # le < ri
                dp[le][ri] = sum(nums[le:ri+1]) - min(dfs(le+1, ri), dfs(le, ri-1))
            return dp[le][ri]
        dfs(0, l-1)
        return 2 * dp[0][l-1] >= sum(nums)
    
# class Solution:
#     def PredictTheWinner(self, nums: List[int]) -> bool:
#         # 经典的二维DP题
#         # 1. 初始化二维DP矩阵
#         l = len(nums)
#         dp = [[0] * l for _ in range(l)]
#         for i in range(l): 
#             dp[i][i] = nums[i]
#         # 2. 找到DP的状态转移方程: j < i 情况下
#         # dp[j][i] = max(nums[j] - dp[j+1][i], nums[i] - dp[j][i-1])
#         # 3. 确定计算方向；计算方向应该与状态转移方程的方向相同。比如这题的状态转移方程中，d[i][j]
#         # 由d[i+1][j]与d[i][j-1]获得，及d[i][j]由其左边与下边元素确定，状态转移方程的方向为左->右与下->上
#         # 因此在计算dp表时也要遵循这个方向
#         # i < j !!!
#         for i in range(l-2, -1, -1):
#             for j in range(i, l):
#                 dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
#         return dp[0][l-1] >= 0