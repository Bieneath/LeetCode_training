# 另一种DP思路，相当棒！
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[] for _ in range(len(s) + 1)] # dp[i]表示s[i:len(s)]这段字符串中所有的分割方案
        dp[-1] = [[]] # dp[len(s):len(s)]这段的所有分割方案为[]
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    for it in dp[j]:
                        dp[i].append([s[i:j]] + it)
        return dp[0]

# # 边DFS+回溯边更新DP表的方法
# from itertools import product
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         l = len(s)
#         ret = []
#         dp = [[None] * l for _ in range(l)]
#         for i, j in product(range(l), range(l)):
#             if i >= j: dp[i][j] = True # dp矩阵左下半三角全设置成True方便编程
#         def dfs(i, path):
#             if i == len(s):
#                 return ret.append(path)
#             for j in range(i, len(s)):
#                 if dp[i][j] is None:
#                     dp[i][j] = True if s[i] == s[j] and dp[i+1][j-1] else False
#                 if dp[i][j]:
#                     dfs(j+1, path + [s[i:j+1]])
#         dfs(0, [])
#         return ret

# # 纯DFS+回溯算法
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         def is_valid(s):
#             return s == s[::-1]
#         ret = []
#         def dfs(s, path):
#             if not s:
#                 return ret.append(path)
#             for i in range(1, len(s)+1):
#                 if is_valid(s[:i]):
#                     dfs(s[i:], path + [s[:i]])
#         dfs(s, [])
#         return ret