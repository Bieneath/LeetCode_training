# DP算法，分析n=2与n=3结果，就能发下n=3是由n=2“套箍”得到。
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [None for _ in range(n+1)]
        dp[0] = ['']
        for i in range(1, n+1):
            cur = []
            for j in range(i):
                for le in dp[j]:
                    for ri in dp[i-j-1]:
                        cur.append('(' + le + ')' + ri)
            dp[i] = cur
        return dp[n]

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