# 逐位比较法
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dis = 0
        for _ in range(32):
            if x&1 != y&1:
                dis += 1
            x >>= 1
            y >>= 1
        return dis

# 汉明距离就是求不同位个数，使用异或直接将相同位变成0，不同位变成1，然后统计1的个数
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y & 0xFFFFFFFF # &0xFFFFFFFF用来防止出现负数时候无限循环！
        dis = 0
        while xor:
            xor &= xor - 1
            dis += 1
        return dis