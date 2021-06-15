# # 递归算法，每遇到一个括号展开一层递归
# class Solution:
#     def calculate(self, s: str) -> int:
#         s += '+' # 为了方便编程
#         def helper(i):
#             ret = num = 0
#             sign = 1
#             while i < len(s) and ')' != s[i]:
#                 if s[i].isdigit():
#                     num = 10 * num + int(s[i])
#                 elif s[i] in ('+', '-'): # 每次遇到符号时候更新累积值，并修改当前值以及符号
#                     ret += sign * num
#                     num = 0
#                     sign = (-1, 1)['+' == s[i]] 
#                 elif '(' == s[i]:
#                     num, i = helper(i + 1)
#                 i += 1
#             return ret + sign * num, i # 返回递归内的值以及递归最后的下标位置
#         return helper(0)[0]

# 使用栈方法，思路是将‘（’之前的累积结果以及符号存放进栈中，与递归思路完全相反
class Solution:
    def calculate(self, s: str) -> int:
        s += '+' # 方便编程
        ret = operand = 0
        sign = 1
        stack = []
        for c in s:
            if c.isdigit():
                operand = 10 * operand + int(c)
            elif c in ('+', '-'):
                ret += sign * operand
                operand = 0
                sign = (-1, 1)[c == '+']
            elif '(' == c:
                stack.extend([ret, sign])
                ret = operand = 0 # 进入括号后，从新计算累积值、操作数和符号
                sign = 1
            elif ')' == c:
                operand = ret + sign * operand # 括号中的结果算作operand!
                sign = stack.pop() # 重新取回括号外的符号
                ret = stack.pop() # 重新取回括号外的累积值
        return ret