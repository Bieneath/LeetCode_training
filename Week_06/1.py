# 遍历1次法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, v in enumerate(nums):
            if target-v in dic:
                return [dic[target-v], i]
            dic[v] = i

# 遍历2次法
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dic = dict()
#         for i, n in enumerate(nums): dic[n] = i
#         for i in range(len(nums)):
#             t = target - nums[i]
#             if t in dic and i != dic[t]:
#                 return [i, dic[t]]
#         # return [-1, -1]{\rtf1}