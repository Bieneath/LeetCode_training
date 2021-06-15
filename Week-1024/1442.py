# import operator
# from itertools import accumulate
# # 前缀异或+暴力搜索
# class Solution:
#     def countTriplets(self, arr: List[int]) -> int:
#         ret = 0
#         acc = [0] + list(accumulate(arr, operator.xor))
#         l = len(acc)
#         for le in range(l):
#             for mid in range(le+1, l):
#                 for ri in range(mid+1, l):
#                     if acc[le] ^ acc[mid] == acc[mid] ^ acc[ri]:
#                         ret += 1
#         return ret

# # 前缀异或+两次循环法
# import operator
# from itertools import accumulate
# class Solution:
#     def countTriplets(self, arr: List[int]) -> int:
#         ret = 0
#         acc = [0] + list(accumulate(arr, operator.xor))
#         l = len(acc)
#         for i in range(l):
#             for j in range(i+1, l):
#                 if acc[i] == acc[j]:
#                     ret += j - i - 1
#         return ret

# 一次遍历法
import operator
from itertools import accumulate
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ret = 0
        acc = [0] + list(accumulate(arr, operator.xor))
        dic = {}
        for i, v in enumerate(acc):
            n, sum_idx = dic.get(v, [0, 0])
            ret += n * i - sum_idx
            dic[v] = [n + 1, sum_idx + i + 1] # 这里是i+1!!!
        return ret