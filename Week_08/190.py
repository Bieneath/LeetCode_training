class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(32):
            digit = n & 1
            n >>= 1
            ret <<= 1
            ret += digit
        return ret