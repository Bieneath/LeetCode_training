# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         ret = 0
#         for i in range(32):
#             # 最低位&运算，看是否是'1'，然后每次n右移一位
#             ret += n & 1
#             n >>= 1
#         return ret

# 方法二： x&(x-1)能清除二进制中最低位的1，所以只要反复做这步，直到n==0就能知道n中有几个1
class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            n &= n-1
            ret += 1
        return ret