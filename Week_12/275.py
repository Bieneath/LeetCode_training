# 二分搜索法
class Solution:
    def hIndex(self, c: List[int]) -> int:
        l = len(c)
        le, ri = 0, l-1
        ret = 0
        while le <= ri:
            mid = le + (ri - le >> 1)
            if c[mid] == l - mid:
                return l - mid
            if c[mid] < l - mid:
                le = mid + 1
            elif c[mid] > l - mid:
                ri = mid - 1
        return l - le   

# # 一遍循环法
# class Solution:
#     def hIndex(self, c: List[int]) -> int:
#         ret = 0
#         for i, v in enumerate(c):
#             if v >= len(c) - i:
#                 ret = len(c) - i
#                 break
#         return ret