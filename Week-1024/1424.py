# 延续498的解题思路，利用下标和排序
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        if not any(nums): return []
        m = len(nums)
        return [nums[i][j] for i, j in \
               sorted([(i, j) for i in range(m) for j in range(len(nums[i]))], \
                     key=lambda x:(x[0]+x[1], x[1]))]