# 使用优先队列探索图，遍历当前点四周的点，将符合条件的点压进优先队列，并根据某种权重排序，因为压入优先队列的都是符合条件的点的周围点，因此某种意义上是根据权重的乱序扩展搜索。因为这个思路相当不错，一定要熟悉一下
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, hq, ret, seen = len(grid), [(grid[0][0], 0, 0)], 0, {0}
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while hq:
            v, i, j = heapq.heappop(hq)
            ret = max(ret, v)
            if i == j == n-1: 
                return ret
            for u, v in dirs:
                x, y = i+u, j+v
                if 0 <= x < n and 0 <= y < n and x*n + y not in seen:
                    seen.add(x*n + y)
                    heapq.heappush(hq, (grid[x][y], x, y))

# # 这题和1631类似
# # 二分搜索+BFS
# from itertools import product
# from collections import deque
# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         MIN, MAX = math.inf, -math.inf
#         dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#         for i, j in product(range(n), range(n)):
#             MAX = max(MAX, grid[i][j])
#             MIN = min(MIN, grid[i][j])
#         def binary_search(left, right):
#             while left <= right:
#                 mid = left + ((right - left) >> 1)
#                 if is_enough(mid):
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             return left
        
#         def is_enough(t):
#             if t < grid[0][0]: return False
#             seen = {0}
#             dq = deque([(0, 0)])
#             while dq:
#                 i, j = dq.popleft()
#                 if i == j == n-1:
#                     return True
#                 for u, v in dirs:
#                     x, y = i+u, j+v
#                     if 0 <= x < n and 0 <= y < n and x*n + y not in seen and t >= grid[x][y]:
#                         seen.add(x*n + y)
#                         dq.append((x, y))
#             return False

#         return binary_search(MIN, MAX)