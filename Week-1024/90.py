# DP算法，如果dp记录所有已近生成的子集，当nums[i]!=nums[i-1]，将nums[i]加到前面所有子集的尾部；当nums[i]==nums[i-1]，将nums[i]只加到nums[i-1]生成的子集尾部。
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        dp = [[]]
        idx = 0
        nums.sort()
        for i, n in enumerate(nums):
            start = 0
            if i > 0 and n == nums[i-1]:
                start = idx
            idx = len(dp)
            for it in dp[start:]:
                dp.append(it + [n])
        return dp

# # 回溯+递归算法
# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         ret = []
#         def dfs(i, path):
#             ret.append(path)
#             if i >= len(nums): return
#             for j in range(i, len(nums)):
#                 if j > i and nums[j-1] == nums[j]: continue
#                 dfs(j + 1, path + [nums[j]])
#         dfs(0, [])
#         return ret