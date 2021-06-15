# from itertools import product
# class Solution:
#     def allCellsDistOrder(self, rows: int, cols: int, r: int, c: int) -> List[List[int]]:
#         def get_dis(p):
#             return abs(p[0] - r) + abs(p[1] - c)
#         points = [[x, y] for x in range(rows) for y in range(cols)]
#         return sorted(points, key=get_dis)

from itertools import product
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, r: int, c: int) -> List[List[int]]:
        return sorted([[x, y] for x, y in product(range(rows), range(cols))], key=lambda x:abs(x[0]-r) + abs(x[1]-c))