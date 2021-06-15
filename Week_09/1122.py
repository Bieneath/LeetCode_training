# from collections import Counter
# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         ret = []
#         dic = Counter(arr1)
#         for n in arr2:
#             ret.extend([n] * dic[n])
#             dic.pop(n)
#         items = sorted(dic.items(), key=lambda x:x[0])
#         for v, c in items:
#             ret.extend([v] * c)
#         return ret

# 参考 https://leetcode.com/problems/relative-sort-array/discuss/334585/Python-Straight-Forward-1-line-and-2-lines 的代码
# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         dic = {v: k for k, v in enumerate(arr2)}
#         return sorted(arr1, key=lambda x:dic.get(x, 1000+x))

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return sorted(arr1, key=(arr2 + sorted(arr1)).index)