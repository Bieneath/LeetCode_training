# # 滑窗一次遍历法
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         if sum(nums) < target: return 0
#         le, ret = 0, float('inf')
#         for ri in range(len(nums)):
#             target -= nums[ri]
#             while target <= 0:
#                 ret = min(ret, ri - le + 1)
#                 target += nums[le]
#                 le += 1
#             if ret == 1: return 1
#         return ret
    
# 二分搜索法+前缀和
import bisect
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        cums = [0] * (len(nums) + 1)
        for i in range(1, len(cums)):
            cums[i] = cums[i-1] + nums[i-1]
        ret = float('inf')
        for i in range(len(cums)):
            idx = bisect.bisect_left(cums, cums[i] + target)
            if idx >= len(cums): break
            ret = min(ret, idx - i)
        return ret
        