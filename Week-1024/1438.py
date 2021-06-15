# 这题最后还是要用双端队列来解才能满足时间复杂度要求；small类似小顶堆，big类似大顶堆
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        small, big = deque(), deque()
        i = ret = 0
        for j, v in enumerate(nums):
            while small and small[-1] > v: # 这里一定要写成>而不能写成>=，允许存在相同的值
                small.pop()
            small.append(v)
            while big and big[-1] < v:
                big.pop()
            big.append(v)
            if big[0] - small[0] > limit:
                if nums[i] == small[0]: small.popleft()
                if nums[i] == big[0]: big.popleft()
                i += 1
        return len(nums) - i # 仔细分析后就能得出i~j的窗口长度就是最长合法子串的长度，j最后到len(nums)-1的位置

# # 使用bisect维护一个有序队列
# import bisect
# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         temp, i = [], 0
#         for n in nums:
#             bisect.insort_left(temp, n)
#             if temp[-1] - temp[0] > limit:
#                 idx = bisect.bisect_left(temp, nums[i])
#                 temp.pop(idx)
#                 i += 1
#         return len(nums) - i

# # https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/solution/he-gua-de-shu-ju-jie-gou-hua-dong-chuang-v46j/ 适合更合适的第三方库来维护一个有序队列；这个库相当不错，但是对API还不是很熟，而且不是python默认库，需要单独pip install
# from sortedcontainers import SortedList
# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         i = 0
#         temp = SortedList()
#         for n in nums:
#             temp.add(n)
#             if temp[-1] - temp[0] > limit:
#                 temp.remove(nums[i])
#                 i += 1
#         return len(nums) - i