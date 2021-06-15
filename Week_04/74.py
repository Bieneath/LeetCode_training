class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        A = []
        for it in matrix:
            A += it
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l + r) // 2
            if A[mid] == target:
                return True
            if A[mid] < target:
                l = mid + 1
            elif A[mid] > target:
                r = mid - 1
        return False