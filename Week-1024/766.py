from itertools import product
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i, j in product(range(m), range(n)):
            if i > 0 and j > 0 and matrix[i][j] != matrix[i-1][j-1]:
                return False
        return True

from itertools import product
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        con = n - 1
        check_45 = [set() for _ in range(m + n - 1)]
        for i, j in product(range(m), range(n)):
            check_45[con - j + i].add(matrix[i][j])
        return all(1 == len(v) for v in check_45)

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(r1[:-1] == r2[1:] for r1, r2 in zip(matrix[:-1], matrix[1:]))