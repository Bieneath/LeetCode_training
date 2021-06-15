# 针对此题的特别解法，参考官方解法四
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        n_rows, n_cols = len(matrix), len(matrix[0])
        i, j = n_rows-1, 0
        while i >=0 and j < n_cols:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target: j += 1
            elif matrix[i][j] > target: i -= 1
        return False

# # 将矩阵合并成一个列表后二分法
# class Solution:
#     def searchMatrix(self, matrix, target):
#         A = []
#         for row in matrix: 
#             A += row
#         A.sort()
#         l, r = 0, len(A)-1
#         while l <= r:
#             mid = l + (r - l)//2
#             if A[mid] == target:
#                 return True
#             elif A[mid] < target:
#                 l = mid + 1
#             elif A[mid] > target:
#                 r = mid - 1
#         return False