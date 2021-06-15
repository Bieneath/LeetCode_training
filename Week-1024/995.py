# https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips/solution/hua-dong-chuang-kou-shi-ben-ti-zui-rong-z403l/ 方法非常非常的巧妙，理解之后题目就不难了
from collections import deque
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        wd = deque()
        ret = 0
        for i, v in enumerate(A):
            if wd and wd[0] + K == i:
                wd.popleft()
            if len(wd)&1 == v: # 此时当前元素必须要翻转！压入划窗
                if i > len(A) - K: return -1 # 当K=3，i=1时候，翻转边界在1+3-1=3上！
                wd.append(i)
                ret += 1
        return ret

# # 直接模拟翻转(超时89/110)
# class Solution:
#     def minKBitFlips(self, A: List[int], k: int) -> int:
#         ret = 0
#         for le in range(len(A) - k + 1):
#             if A[le] == 0:
#                 for i in range(k):
#                     A[le+i] ^= 1
#                 ret += 1
#         return -1 if 0 in A[le:] else ret