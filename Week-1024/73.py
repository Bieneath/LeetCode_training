# O(1)空间消耗的算法；使用r和c记录第一行与第一列是否需要置0，使用第一行与第一列完成类似check_row, check_col的工作
from itertools import product
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        r, c = False, False
        for i in range(m):
            if 0 == matrix[i][0]:
                c = True
                break
        for j in range(n):
            if 0 == matrix[0][j]:
                r = True
                break
        for i, j in product(range(1, m), range(1, n)):
            if 0 == matrix[i][j]:
                matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m): # 第一行和第一列不要动！！！
            if 0 == matrix[i][0]:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n): # 第一行和第一列不要动！！！
            if 0 == matrix[0][j]:
                for i in range(1, m):
                    matrix[i][j] = 0
        if c:
            for i in range(m):
                matrix[i][0] = 0
        if r:
            for j in range(n):
                matrix[0][j] = 0

# # 常规策略
# from itertools import product
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         m, n = len(matrix), len(matrix[0])
#         rows, cols = [True] * m, [True] * n
#         for i, j in product(range(m), range(n)):
#             if matrix[i][j] == 0:
#                 rows[i] = cols[j] = False
#         for i, j in product(range(m), range(n)):
#             if not rows[i] or not cols[j]:
#                 matrix[i][j] = 0