# 牛顿法
class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        r = n
        e = 1e-5
        while r*r > n:
            r = (r + n/r) // 2
            # print(r)
        return abs(r*r - n) < e

# 二分法
# class Solution:
#     def isPerfectSquare(self, n: int) -> bool:
#         l, r = 0, n
#         while l <= r:
#             mid = l + (r - l)//2
#             if mid**2 == n:
#                 return True
#             if mid**2 < n:
#                 l = mid + 1
#             elif mid**2 > n:
#                 r = mid - 1
#         return False