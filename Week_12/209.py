# class Solution:
#     def minSubArrayLen(self, s: int, nums: List[int]) -> int:
#         def bi_search(A, target):
#             le, ri = 0, len(A) - 1
#             while le <= ri:
#                 mid = le + (ri - le >> 1)
#                 if target == A[mid]:
#                     return mid
#                 if target < A[mid]:
#                     ri = mid - 1
#                 elif target > A[mid]:
#                     le = mid + 1
#             return le
        
#         ret = float('inf')
#         # 求前缀和
#         cum = [0] * len(nums) + [0]
#         cum[0] = 0
#         for i in range(1, len(cum)):
#             cum[i] = cum[i-1] + nums[i-1]
#         for le, v in enumerate(cum):
#             # 使用二分搜索确定ri的下标
#             ri = bi_search(cum, v + s)
#             if ri < len(cum):
#                 ret = min(ret, ri - le)
#         return 0 if ret == float('inf') else ret    

# 使用python内置的bisect方法进行二分搜索，提升滑窗右边框的定位速度
import bisect
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ret = float('inf')
        # 求前缀和
        cum = [0]
        for n in nums:
            cum.append(cum[-1] + n)
        for le, v in enumerate(cum):
            # 使用二分搜索确定ri的下标
            ri = bisect.bisect_left(cum, v + s)
            if ri < len(cum):
                ret = min(ret, ri - le)
        return 0 if ret == float('inf') else ret              

# # 比较好的滑窗算法(一次遍历法)
# class Solution:
#     def minSubArrayLen(self, s: int, nums: List[int]) -> int:
#         le = 0
#         ret = float('inf')
#         for ri, v in enumerate(nums):
#             s -= v
#             while s <= 0:
#                 ret = min(ret, ri - le + 1)
#                 s += nums[le]
#                 le += 1
#         return 0 if ret == float('inf') else ret
        
# # # 基础版的滑窗搜索法
# class Solution:
#     def minSubArrayLen(self, s: int, nums: List[int]) -> int:
#         if not nums: return 0
#         cum = [0] * (len(nums) + 1)
#         cum[0] = 0
#         for i in range(1, len(cum)):
#             cum[i] = cum[i-1] + nums[i-1]
#         i, j = 0, 1
#         ret = float('inf')
#         while j < len(cum):
#             while cum[j] - cum[i] >= s:
#                 ret = min(ret, j - i)
#                 i += 1
#             j += 1
#         return 0 if ret == float('inf') else ret
                