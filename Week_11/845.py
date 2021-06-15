# 一遍遍历法，使用up和down记录上坡和下坡长度
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        ret = up = down = 0
        for i in range(1, len(A)):
            if down and A[i-1] < A[i] or A[i-1] == A[i]:
                up = down = 0
            up += A[i-1] < A[i]
            down += A[i-1] > A[i]
            if up and down: ret = max(ret, up + down + 1)
        return ret

# 正反两遍遍历法，每次都记录上升子数组长度
# class Solution:
#     def longestMountain(self, A: List[int]) -> int:
#         l = len(A)
#         rev = [0] * l
#         ret = 0
#         for i in range(1, l):
#             if A[i] > A[i-1]:
#                 rev[i] = rev[i-1] + 1
#         count = 0
#         for i in range(l-2, -1, -1):
#             if A[i] > A[i+1]:
#                 count += 1
#                 if rev[i]:
#                     rev[i] += count
#                 ret = max(ret, rev[i])
#             else:
#                 count = 0
#         return ret + 1 if ret else 0