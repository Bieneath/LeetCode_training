# 归并排序算法，这题因为要返回的是一个counts列表，所以要把最初的下标和元素值对应上。可参考 https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution
from collections import deque
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = list(enumerate(nums))
        counts = [0] * len(nums)
        def daq(le, ri):
            if le >= ri: return nums[le:ri+1]
            mid = (le + ri) >> 1
            right = daq(mid+1, ri)
            left = daq(le, mid)
            ret = deque()
            while True:
                if not left:
                    return right + list(ret)
                if not right:
                    return left + list(ret)
                if left[-1][1] > right[-1][1]:
                    counts[left[-1][0]] += len(right)
                    ret.appendleft(left.pop())
                else:
                    ret.appendleft(right.pop())
            return list(ret)
        daq(0, len(nums) - 1)
        return counts

# # 这题用归并不好做
# from sortedcontainers import SortedList
# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         ret = [0] * len(nums)
#         sortedlist = SortedList()
#         for i in range(len(nums)-1, -1, -1):
#             idx = sortedlist.bisect_left(nums[i])
#             sortedlist.add(nums[i])
#             ret[i] = idx
#         return ret