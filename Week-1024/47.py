# # 使用API
# from itertools import permutations
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         return list(set(permutations(nums)))

# # 排序+递归+回溯
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         # 第一步是排序，其实是为了将相同的字母聚在一起，方便去重
#         nums.sort()
#         ret = []
#         def dfs(nums, path):
#             if not nums:
#                 ret.append(path)
#             for i, n in enumerate(nums):
#                 if i > 0 and n == nums[i-1]: continue # 去重
#                 dfs(nums[:i] + nums[i+1:], path + [n])
#         dfs(nums, [])
#         return ret

# 首先要明白排列的概念，给定数字1, 2, 3，包括的排列有
# [1, 2, 3] [1, 3, 2] [2, 1, 3] [2, 3, 1] [3, 1, 2] [3, 2, 1]
# 如下的算法是根据先确定1，再确定2的各个位置，然后再确定3的各个位置。
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for n in nums: # 遍历nums作为循环的最外层，也是让整个循环结束的方法
            new_ans = []
            for it in ret:
                for i in range(len(it) + 1):
                    new_ans.append(it[:i] + [n] + it[i:])
                    # 重复的数字只插在前面，因为it[i]这个数字会往后排。
                    if i < len(it) and n == it[i]:
                        break
            ret = new_ans
        return ret