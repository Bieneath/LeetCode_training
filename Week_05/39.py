# 递归回溯算法
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def helper(i, SUM, path):
            if SUM == target:
                ret.append(path)
                return
            if SUM > target:
                return
            for j in range(i, len(candidates)):
                helper(j, SUM + candidates[j], path + [candidates[j]])
        helper(0, 0, [])
        return ret

# 我最初提交的算法修正方案
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         ret = []
#         def helper(i, SUM, path):
#             SUM += candidates[i]
#             path += [candidates[i]]
#             if SUM == target:
#                 ret.append(path)
#                 return
#             if SUM > target:
#                 return
#             for j in range(i, len(candidates)):
#                 helper(j, SUM, path[:])
#         for i in range(len(candidates)):
#             helper(i, 0, [])
#         return ret