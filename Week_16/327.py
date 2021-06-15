# 前缀和+分治+归并排序；和497类似
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pre = [0]
        for n in nums:
            pre.append(pre[-1] + n)
        def helper(nums):
            if len(nums) < 2:
                return 0
            mid = len(nums) >> 1
            ret = 0
            ret += helper(nums[:mid]) + helper(nums[mid:])
            nums[:] = sorted(nums[:mid]) + sorted(nums[mid:])
            le = ri = mid
            for v in nums[:mid]:
                while le < len(nums) and nums[le] - v < lower: le += 1
                while ri < len(nums) and nums[ri] - v <= upper: ri += 1
                ret += ri - le
            return ret
        return helper(pre)

# 前缀和+分治+归并排序；和497类似
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pre = [0]
        # 前缀和数组，第一个元素为0，方便计算
        # 使用前缀和数组将问题转换为求lower <= pre[idx2] - pre[idx1] <= upper的问题
        for n in nums:
            pre.append(pre[-1] + n)
        def helper(le, ri):
            mid = le + (ri - le >> 1)
            if mid == le: return 0
            count = helper(le, mid) + helper(mid, ri)
            i = j = mid
            # pre[le:mid]和pre[mid:ri]都是升序数组
            for v in pre[le:mid]: # 这里是提速的原理所在，随着v的右移，新的满足条件的i和j只可能在原来的i和j的右侧，左侧的情况不必再被探索
                while i < ri and pre[i] - v < lower: i += 1 # 这里循环嵌套两个串行的循环，i和j其实只遍历[mid:ri]一次。
                while j < ri and pre[j] - v <= upper: j += 1
                count += j - i
            pre[le:ri] = sorted(pre[le:ri]) # 归并左右两部分，并让归并后的数组变成升序
            return count
        return helper(0, len(pre))

# # 普通前缀和方法（超时）
# class Solution:
#     def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
#         if not nums: return 0
#         l = len(nums)
#         count = 0
#         cum = [0] * (l + 1)
#         cum[1] = nums[0]
#         for i in range(1, l + 1):
#             cum[i] = cum[i-1] + nums[i - 1]
#         for i in range(1, l + 1):
#             for j in range(i):
#                 if lower <= cum[i] - cum[j] <= upper:
#                     count += 1
#         return count