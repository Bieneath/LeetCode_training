class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret = count = 0
        for n in nums:
            if not n:
                ret = max(ret, count)
                count = 0
            else:
                count += 1
        return max(ret, count)

# # 使用itertools.groupby API
# from itertools import groupby
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         return max(sum(x) for _, x in groupby(nums))