# 这题就是DP问题中保留上个路径的类问题，类似爬楼梯。但是难点在于要想清楚一些问题，其中之一就是根据上一步的所有结果，推出当前步的结果，t[x] = t[x-n]+t[x+n]，这里有两点，第一是有哪些x是根据上一步得出的，而不是通过x反推x-n与x+n；其二是这题只保存当前结果，而不保存之前的结果，比如1, 10这个列表，第一步结果1的路径在最后是没有意义的，因为1和10最后不可能出现1的结果。因此每次只保留当前步的所有结果！
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dd = defaultdict(int)
        dd[0] = 1
        for n in nums:
            temp = defaultdict(int) # 由于只保留从前一步推出的当前步结果，因此temp新建一个空字典
            for k in dd:
                temp[k+n] += dd[k]
                temp[k-n] += dd[k]
            dd = temp
        return dd[target]