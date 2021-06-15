# 递归+生成器
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(le, ri, s):
            if 0 == ri: yield s
            if le > 0:
                for x in generate(le - 1, ri, s + '('):
                    yield x
            if ri > le:
                for x in generate(le, ri - 1, s + ')'):
                    yield x
        return list(generate(n, n, ''))

# # DP版本，这题的DP思路很难想到。dp[n]及n对合法括号对组成方式是与dp[a]与dp[b]相关，其中a+b = n-1。a取值[0, n-1]，b取值[n-1, 0]
from itertools import product
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # dp[0]的情况，就是一个空字符串''
        dp = [['']]
        for k in range(1, n + 1):
            cur = []
            for i in range(0, k):
                j = k - 1 - i # 因为要加上一对()，所以i + j必须等于k - 1
                for le, ri in product(dp[i], dp[j]):
                    cur.append('(' + le + ')' + ri)
            dp.append(cur)
        return dp[-1]