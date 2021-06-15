# 所谓2的幂次方就是二进制中只有1位是1
# API方法1
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # '{:032b}'.format(n)会直接返回n的二进制字符串形式，同时高位补0
        return n > 0 and '{:b}'.format(n).count('1') == 1

# API方法2
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         # bin(16)输出的是一个字符串"0b10000"
#         return n > 0 and bin(n).count('1') == 1

# 数学
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        return (n & n-1) == 0