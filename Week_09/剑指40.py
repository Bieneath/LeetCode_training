import heapq
from heapq import heappop, heappush
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # ret = h = [] # 这种初始化方法是非常非常危险的！
        # python中的heapq弹出的是最小值
        ret, h = [], []
        for it in arr:
            heappush(h, it)
        for _ in range(k):
            ret.append(heappop(h))
        return ret