class Solution
    def checkStraightLine(self, coordinates List[List[int]]) - bool
        n1 = coordinates[1][0] - coordinates[0][0]
        n2 = coordinates[1][1] - coordinates[0][1]
        for x, y in coordinates[2]
            if n1  (y - coordinates[0][1]) != n2  (x - coordinates[0][0])
                return False
        return True

# class Solution
#     def checkStraightLine(self, coordinates List[List[int]]) - bool
#         a = b = None
#         n1 = coordinates[1][1] - coordinates[0][1]
#         n2 = coordinates[1][0] - coordinates[0][0]
#         if n2
#             a = n1  n2
#             b = coordinates[0][1] - a  coordinates[0][0]
#         threshold = 1e-3
#         for x, y in coordinates[2]
#             if a is not None
#                 if abs(ax + b - y) = threshold
#                     return False
#             else
#                 if x != coordinates[0][0]
#                     return False
#         return True