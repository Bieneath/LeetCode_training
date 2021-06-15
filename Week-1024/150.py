# 遇到操作符就从栈中弹出两个值
from operator import add, sub, mul, truediv
from functools import reduce
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = dict([('+', add), ('-', sub), ('*', mul), ('/', truediv)])
        for it in tokens:
            if it in op:
                n2 = stack.pop()
                n1 = stack.pop()
                res = reduce(op[it], [n1, n2])
                stack.append(int(res))
            else:
                stack.append(int(it))
        return stack.pop()