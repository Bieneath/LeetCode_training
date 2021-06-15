# 仔细分析这题的规律，就能发现所有数按位与后，能活下来的1一定是m与n从左边开始共有的前缀和1的长度，因此只要直到共有的前缀1有多长，在哪里就行了。
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        while m != n:
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift

# # 超时
# from functools import reduce
# import operator
# class Solution:
#     def rangeBitwiseAnd(self, m: int, n: int) -> int:
#         return reduce(operator.and_, range(m, n+1))