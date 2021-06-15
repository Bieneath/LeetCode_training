# class Solution:
#     def addDigits(self, num: int) -> int:
#         d = carry = 0
#         while num:
#             t = num % 10
#             d = (d+t)%10 + (d+t)//10
#             num //= 10
#         return d

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        t = num % 9
        if not t: t = 9
        return t