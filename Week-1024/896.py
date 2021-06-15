class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        flag = True if A[0] < A[-1] else False
        for a, b in zip(A, A[1:]):
            if (flag and a > b) or (not flag and a < b):
                return False
        return True