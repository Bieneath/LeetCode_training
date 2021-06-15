# 560与363题思路的结合问题
from itertools import accumulate
import operator
from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        # 先求行方向的前缀和矩阵
        matrix = [list(accumulate(row, operator.add)) for row in matrix] # accumulate(iterable, method)
        # 枚举所有的列的左右边界，然后让列降维到1维，此时每个枚举都是长度为行数的一维列表，在使用#560的哈希表算法
        ret = 0
        for le in range(n):
            for ri in range(le, n):
                # 以下与#560解法一模一样
                dic = defaultdict(int)
                dic[0] = 1 # 累积和为0的有一个，初始情况
                acc = 0
                for i in range(m):
                    cur = matrix[i][ri] - (matrix[i][le-1] if le > 0 else 0)
                    acc += cur
                    # 以下两行不能调换顺序！比如target=0，只计算当前acc之前出现acc的次数！
                    ret += dic[acc - target]
                    dic[acc] += 1
        return ret