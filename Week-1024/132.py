# 嵌套DP，需要两个DP才能解
from itertools import product
class Solution:
    def minCut(self, s: str) -> int:
        l = len(s)
        # 第一个DP：构建下标和是否是回文字符串的对照DP表
        is_par = [[None] * l for _ in range(l)]
        for i, j in product(range(l), range(l)):
            if i >= j: is_par[i][j] = True
        # 构建DP表先让j遍历[0, l]，然后让i遍历[0, i]，这个顺序不能错！
        for j in range(1, l):
            for i in range(j):
                is_par[i][j] = True if s[i] == s[j] and is_par[i+1][j-1] else False
        # 第二个DP：使用DP列表保存[0, i]范围内最小的段落数
        min_sect = [x+1 for x in range(l)] + [0] # 给min_sect[-1]设置为0，方便后续编程
        for j in range(1, l):
            for i in range(j + 1): # 这里i与j一定要重合一次！
                if is_par[i][j]:
                    min_sect[j] = min(min_sect[j], min_sect[i-1] + 1)
                    if min_sect[j] == 1: break # 已近达到最小值1，直接break
        return min_sect[-2] - 1