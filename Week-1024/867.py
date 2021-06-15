# 使用zip完成矩阵转置
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(line) for line in zip(*matrix)]

# import numpy as np
# class Solution:
#     def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
#         matrix = np.array(matrix)
#         return matrix.T.tolist()