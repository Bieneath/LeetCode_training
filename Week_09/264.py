# 使用堆的方法，更加逻辑清晰，简单易懂
from heapq import heapify, heappush, heappop
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ret = []
        hp = [1]
        check = {1}
        heapify(hp)
        while len(ret) < n:
            num = heappop(hp)
            ret.append(num)
            for it in [2, 3, 5]:
                if num * it not in check:
                    check.add(num * it)
                    # 堆插入是要消耗时间的，所以在插入前先检查一下
                    heappush(hp, num * it) 
        return ret[-1]

# # DP方法，有几个坑，容易写错
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         if n < 1: return None
#         ret = [1]
#         n2, n3, n5 = 2, 3, 5
#         i2 = i3 = i5 = 0
#         for _ in range(1, n):
#             v2 = n2 * ret[i2]
#             v3 = n3 * ret[i3]
#             v5 = n5 * ret[i5]
#             min_v = min(v2, v3, v5)
#             # 下面三个分支不能用if...elif...elif，因为n2,n3,n5中可能有多个等于v！
#             if min_v == v2:
#                 i2 += 1
#             if min_v == v3:
#                 i3 += 1
#             if min_v == v5:
#                 i5 += 1
#             ret.append(min_v)
#         return ret[-1]