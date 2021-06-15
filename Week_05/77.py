# # 手动实现
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         combs = [[]]
#         for i in range(k):
#             combs = [cb + [d] for cb in combs for d in range(cb[-1]+1 if cb else 1, n+1)]
#         return combs

# 使用python API
import itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [x for x in itertools.combinations(range(1, n+1), k)]