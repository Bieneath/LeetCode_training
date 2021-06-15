# reduce(func, iter, init)；循环嵌套func(rev, x)函数:func(func(func()))，其中第二个参数iter为一个可迭代数据，每次都会从其中取出一个元素放入func中进行运算，放入的位置是x；init为初始化值，及第一次迭代时候的rev。
from functools import reduce
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(ret, c):
            if '#' == c:
                if ret: ret.pop()
            else: ret.append(c)
            return ret
        return reduce(helper, S, []) == reduce(helper, T, [])