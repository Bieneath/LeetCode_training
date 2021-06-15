class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ret = map(lambda x:x**2, A)
        return sorted(ret)