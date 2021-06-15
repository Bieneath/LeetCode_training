# 讨论区大佬的解法
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [0]
        ret = 0
        for c in s:
            if '(' == c:
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    ret = max(ret, stack[-1])
                else:
                    stack = [0]
        return ret

# # 自己的解法
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         ret = 0
#         l = len(s)
#         dp = [0] * l
#         stack = []
#         for i in range(l):
#             if not stack or '(' == s[i] or stack[-1][0] == s[i]:
#                 stack.append((s[i], i))
#             else: # stack[-1][0] == '(' and s[i] == ')'
#                 idx = stack[-1][1]
#                 # i - idx + 1计算当前合法的括号长度；dp[idx-1] if idx > 0 else 0是查看能否衔接上前面的有效括号长度
#                 dp[i] = i - idx + 1 + (dp[idx-1] if idx > 0 else 0)
#                 ret = max(ret, dp[i])
#                 stack.pop()
#         return ret