# DP版本，这题的DP思路很难想到。dp[n]及n对合法括号对组成方式是与dp[a]与dp[b]相关，其中a+b = n-1。a取值[0, n-1]，b取值[n-1, 0]
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [['']]
        for k in range(1, n + 1):
            cur = []
            for i in range(k):
                j = k - 1 - i
                for le in dp[i]:
                    for ri in dp[j]:
                        cur.append('(' + le + ')' + ri)
            dp.append(cur)
        return dp[-1]

# # 递归解法
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         ret = []
#         def dfs(s, le, ri):
#             if ri == n:
#                 ret.append(s)
#                 return
#             if le < n:
#                 dfs(s + '(', le + 1, ri)
#             if ri < le:
#                 dfs(s + ')', le, ri + 1)
#         dfs('', 0, 0)
#         return ret

#  # 递归解法（生成器版），牛x，我终于想明白算法原理了。
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         def generate(s, le, ri):
#             if not ri:
#                 yield s
#             if le > 0:
#                 for x in generate(s + '(', le - 1, ri):
#                     yield x
#             if ri > le:
#                 for x in generate(s + ')', le, ri - 1):
#                     yield x
#         return list(generate('', n, n))