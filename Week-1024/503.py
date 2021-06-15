# 找下一个最大值可以用栈来完成
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ret = [-1] * l
        stack = []
        nums *= 2
        for i, v in enumerate(nums):
            while stack and nums[stack[-1]] < v:
                idx = stack.pop() % l
                ret[idx] = v
            stack.append(i)
        return ret
 
# # 与上面相同的解法，只是有个比较有趣的技巧
# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         l = len(nums)
#         stack = []
#         ret = [-1] * l
#         for i in list(range(l)) * 2:
#             while stack and nums[stack[-1]] < nums[i]:
#                 ret[stack.pop()] = nums[i]
#             stack.append(i)
#         return ret