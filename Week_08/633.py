# import math
# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         def isSquare(x):
#             return int(x**0.5)**2 == x
#         return any(isSquare(c - n**2) for n in range(int(c**0.5) + 1))

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(c**.5)
        while a <= b:
            v = a**2 + b**2
            if v == c:
                return True
            if v < c:
                a += 1
            elif v > c:
                b -= 1
        return False