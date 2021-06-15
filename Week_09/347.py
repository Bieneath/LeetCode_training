# 使用堆来解
from heapq import heapify, heappush, heappop
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        hp = []
        for i, v in dic.items(): # 这里当心别用k, v，因为k这个变量已经被占用了
            heappush(hp, (v, i))
            if len(hp) > k:
                heappop(hp)
        ret = [it[1] for it in hp]
        return ret[::-1]

# # 使用字典+sorted()函数
# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         ret = []
#         dic = Counter(nums)
#         items = sorted(dic.items(), key=lambda x:x[1], reverse=True)
#         ret.extend([items[i][0] for i in range(k)])
#         return ret