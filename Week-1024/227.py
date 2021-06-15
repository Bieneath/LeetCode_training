# 227的解题思路和224几乎不同，因为224是遇到(进栈或函数，存在多重栈或者函数嵌套，而227只需要一个栈，因为最多也就只会嵌套一层，即乘和除优先于加减
class Solution:
    def calculate(self, s: str) -> int:
        s += '+' # 方便编程
        stack = []
        sign = '+'
        operand = 0
        for c in s:
            if c.isdigit():
                operand = operand * 10 + int(c)
            elif c in {'+', '-', '*', '/'}:
                if '+' == sign:
                    stack.append(operand)
                elif '-' == sign:
                    stack.append(-operand)
                elif '*' == sign:
                    stack.append(stack.pop() * operand) # 这个解法最精妙的地方就是这里，将数字压进栈，遇到*或/弹出栈尾参与计算即可
                elif '/' == sign: # 这里除法部分有点要注意，python中//默认是向下取整，比如-3//2=-2，这就和题目要求不一致了，所以要用int(-3/2)
                    stack.append(int(stack.pop() / operand))
                sign = c
                operand = 0
        return sum(stack)