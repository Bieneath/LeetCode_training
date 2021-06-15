# # 通过bisect维护一个有序列表，并通过该列表查出有多少个比当前数大的数字。
# import bisect
# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         ret = 0
#         sorted_list = []
#         for n in nums:
#             idx = bisect.bisect_right(sorted_list, n)
#             ret += len(sorted_list) - idx
#             sorted_list.insert(idx, n)
#         return ret

# # 使用第三方模块SortedList来维护一个有序列表
# from sortedcontainers import SortedList
# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         sorted_list = SortedList()
#         ret = 0
#         for n in nums:
#             idx = sorted_list.bisect_right(n)
#             ret += len(sorted_list) - idx
#             sorted_list.add(n)
#         return ret

# 分治+归并排序(merge sort)；解题思路 https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/shu-zu-zhong-de-ni-xu-dui-by-leetcode-solution/
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ret = [0]
        def daq(nums):
            # 分治部分
            if len(nums) <= 1: return nums
            mid = len(nums) >> 1
            left = daq(nums[:mid])
            right = daq(nums[mid:])
            # 归并排序部分
            merge = []
            i = j = 0
            while True:
                if i == len(left):
                    return merge + right[j:]
                if j == len(right):
                    return merge + left[i:]
                if left[i] > right[j]:
                    ret[0] += len(left) - i
                    merge.append(right[j])
                    j += 1
                else:
                    merge.append(left[i])
                    i += 1
        daq(nums)
        return ret[0]