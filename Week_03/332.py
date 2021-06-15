from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dd = defaultdict(list)
        for k, v in tickets: dd[k].append(v)
        for k in dd.keys():
            heapq.heapify(dd[k]) # 这里就是最经典的地方，用heapq对字典的value列表进行排序，达到按字符排序的效果
        ret = []
        def dfs(airport):
            while dd[airport]:
                temp = heapq.heappop(dd[airport])
                dfs(temp)
            ret.append(airport)
        dfs('JFK')
        return ret[::-1]