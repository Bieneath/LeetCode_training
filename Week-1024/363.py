# https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/gu-ding-zuo-you-bian-jie-qian-zhui-he-er-fen-by-po/
# 这题真瘠薄难，建议多参考一下别人写的攻略；由于行数远超列数，因此尽可能在列上使用二分搜索！先确定左右边界，然后再对左右边界之间的数字逐行求前缀和
import bisect
from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ret = -math.inf
        m, n = len(matrix), len(matrix[0])
        # 先保证行数>列数
        if m < n:
            matrix = list(zip(*matrix))
        m, n = max(m, n), min(m, n)
        for le in range(n):
            pre_sum = [0] * m
            for ri in range(le, n):
                for r in range(m):
                    pre_sum[r] += matrix[r][ri]
                arr = [0, math.inf] # 0是必须加的，inf是防止idx出界
                cur_sum = 0
                for x in pre_sum:
                    cur_sum += x
                    idx = bisect.bisect_left(arr, cur_sum - k)
                    ret = max(ret, cur_sum - arr[idx])
                    if ret == k: return k
                    bisect.insort(arr, cur_sum) # 使用bisect.insort()来维护一个有序列表arr
        return ret