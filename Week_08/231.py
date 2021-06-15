# 所谓2的幂次就是n的二进制形式中只有一个1
# 方法一，使用bin方法将十进制转为二进制，注意bin()返回的是str
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and 1 == bin(n).count('1')
        
# 方法二，利用n & (n-1)去掉最低位1的特性
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not n&(n-1)