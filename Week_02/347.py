import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        dic = collections.Counter(nums)
        dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            ret.append(dic[i][0])
        return ret