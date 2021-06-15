# class Solution:
#     def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
#         def transfer(line):
#             le, ri = 0, len(line) - 1
#             while le <= ri:
#                 line[le], line[ri] = line[ri]^1, line[le]^1
#                 le += 1
#                 ri -= 1
#         for line in A:
#             transfer(line)
#         return A

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[1^x for x in reversed(y)] for y in A]