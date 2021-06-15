# 解题思路 https://www.youtube.com/watch?v=cJayBq38VYw
import heapq
from itertools import product
class Solution:
    def trapRainWater(self, hs: List[List[int]]) -> int:
        if len(hs) < 3 or len(hs[0]) < 3: return 0
        m, n = len(hs), len(hs[0])
        hq, dirs = [], [(-1, 0), (1, 0), (0, -1), (0, 1)]
        water = level = 0
        for i, j in product([0, m-1], range(n)):
            heapq.heappush(hq, (hs[i][j], i, j))
            hs[i][j] = '#'
        for i, j in product(range(1, m-1), [0, n-1]):
            heapq.heappush(hq, (hs[i][j], i, j))
            hs[i][j] = '#'
        while hq:
            h, i, j = heapq.heappop(hq)
            level = max(level, h)
            for u, v in dirs:
                if 0 <= i+u < m and 0 <= j+v < n and '#' != hs[i+u][j+v]:
                    value = hs[i+u][j+v]
                    hs[i+u][j+v] = '#'
                    water += max(0, level - value)
                    heapq.heappush(hq, (value, i+u, j+v))
        return water