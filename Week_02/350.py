from collections import Counter

# 计数解法;统计n1中不同数字出现的次数，再搜索n2，看看有没有相同的数字
class Solution:
    def intersect(self, n1: List[int], n2: List[int]) -> List[int]:
        ret = []
        counts = Counter(n1)
        for it in n2:
            if counts.get(it, 0) > 0:
                counts[it] -= 1
                ret.append(it)
        return ret

# 双指针解法
# class Solution:
#     def intersect(self, n1: List[int], n2: List[int]) -> List[int]:
#         n1.sort()
#         n2.sort()
#         p1 = p2 = 0
#         ret = []
#         while p1 < len(n1) and p2 < len(n2):
#             if n1[p1] == n2[p2]:
#                 ret.append(n1[p1])
#                 p1 += 1
#                 p2 += 1
#             elif n1[p1] < n2[p2]:
#                 p1 += 1
#             else: # n1[p1] > n2[p2]
#                 p2 += 1
#         return ret