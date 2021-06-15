# 这题的基本思路还是维护一个以腐烂日期为基准的排序堆，随着天数增长查看堆中是否还有合格的苹果。
# 话虽如此，代码却很不好写，需要注意很多细节部分。
import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        hq = []
        count, i = 0, 1 # 为何更加符合逻辑，i从1开始计数
        while hq or i < (len(apples) + 1): # 1~len(apples)
            if i < (len(apples) + 1):
                a, d = apples[i-1], days[i-1]
                heapq.heappush(hq, [i + d - 1, a]) # 注意i+days[i]是腐烂的这一天，已近不能吃了，所以要-1
            while hq and (hq[0][0] < i or hq[0][1] == 0): # 从hq中去除已经腐烂的以及被吃完的苹果
                heapq.heappop(hq)
            if hq:
                hq[0][1] -= 1
                count += 1
            i += 1
        return count