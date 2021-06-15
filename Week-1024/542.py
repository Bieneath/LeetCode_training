# https://leetcode.com/problems/01-matrix/discuss/101102/Short-solution-Each-path-needs-at-most-one-turn 顺时针旋转4次的方法
# 如何顺时针，逆时针90度旋转矩阵方法非常值得学习
# t = [[1, 2], [3, 4]]
# 顺时针旋转90度
# t2 = list(map(list, zip(*t[::-1])))
# 逆时针旋转90度
# t3 = list(map(list, zip(*t)))[::-1]

# 多次DP
from itertools import product
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ret = [[float('inf')] * n for _ in range(m)]
        # 第一次DP遍历，从左上往右下
        for i, j in product(range(m), range(n)):
            if matrix[i][j]:
                c = float('inf') if i == 0 else ret[i-1][j] + 1
                r = float('inf') if j == 0 else ret[i][j-1] + 1
                ret[i][j] = min(c, r)
            else:
                ret[i][j] = 0
        # 第二次DP遍历，从右下往左上
        for i, j in product(range(m-1, -1, -1), range(n-1, -1, -1)):
            if ret[i][j] > 0:
                c = float('inf') if i == m-1 else ret[i+1][j] + 1
                r = float('inf') if j == n-1 else ret[i][j+1] + 1
                ret[i][j] = min(ret[i][j], c, r)
        return ret

# from itertools import product
# from collections import deque
# # 多源BFS搜索
# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         m, n = len(matrix), len(matrix[0])
#         check = [[True] * n for _ in range(m)]
#         dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#         dq = deque()
#         for i, j in product(range(m), range(n)):
#             if matrix[i][j] == 0:
#                 dq.append((i, j))
#                 check[i][j] = False
#         step = 0
#         while dq:
#             sz = len(dq)
#             for _ in range(sz):
#                 x, y = dq.popleft()
#                 matrix[x][y] = step
#                 for u, v in dirs:
#                     if 0 <= x+u < m and 0 <= y+v < n and check[x+u][y+v]:
#                         dq.append((x+u, y+v))
#                         check[x+u][y+v] = False
#             step += 1
#         return matrix
        
# # 普通BFS
# from itertools import product
# from collections import deque
# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         m, n = len(matrix), len(matrix[0])
#         dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#         ret = [[-1] * n for _ in range(m)]
#         for i, j in product(range(m), range(n)):
#             if 0 == matrix[i][j]:
#                 ret[i][j] = 0

#         def bfs(i, j):
#             dq = deque([(i, j)])
#             count = 0
#             seen = {(i, j)}
#             while dq:
#                 sz = len(dq)
#                 for _ in range(sz):
#                     x, y = dq.popleft()
#                     if ret[x][y] == 0:
#                         return count
#                     for u, v in dirs:
#                         if 0 <= x+u < m and 0 <= y+v < n and (x+u, y+v) not in seen:
#                             dq.append((x+u, y+v))
#                             seen.add((x+u, y+v))
#                 count += 1

#         for i, j in product(range(m), range(n)):
#             if -1 == ret[i][j]:
#                 ret[i][j] = bfs(i, j)
#         return ret