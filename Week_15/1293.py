# 这题有个减枝逻辑，当前i, j如果满足m - i + n - j - 3 <= k时，表示k完全有能力去除所有最短路径上的障碍，此时最短路径是m - i + n - j - 2
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 3: return m + n - 2
        start = (m-1, n-1, k) # 为了方便减枝，我们将起点挪到右下角，终点改成左上角
        seen = {start} # 这里是这题的一个核心点，怎么避免走重复的路线，光通过i, j不够，还要加上k，及如果走过重复点grid[i][j]，而且剩余k数量也一致，那么就没必要继续探索了。
        dq = deque([start])
        count = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                i, j, b = dq.popleft()
                if not i and not j:
                    return count
                b -= grid[i][j]
                if b < 0: continue
                for u, v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_state = (i+u, j+v, b)
                    if 0 <= i+u < m and 0 <= j+v < n and next_state not in seen:
                        dq.append(next_state)
                        seen.add(next_state)
            count += 1
        return -1