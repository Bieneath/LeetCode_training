# # 基于摩尔投票法，原理就是最多的元素（>n/2）能在零和游戏中存活下来
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         candidate, votes = nums[0], 0
#         for n in nums:
#             if votes == 0 and candidate != n:
#                 candidate = n
#             if n == candidate: votes += 1
#             else: votes -= 1
#         return candidate

# 基于排序后取中间值
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]