# dp[i]由dp[i-n] + dp[i+n]组成，如果没有汇合，所有节点的路线都为1
# 参考官方题解思路(动态图)。
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dd = defaultdict(int)
        dd[0] = 1
        for x in nums:
            step = defaultdict(int)
            for y in dd:
                step[y + x] += dd[y]
                step[y - x] += dd[y]
            dd = step
        return dd[S]