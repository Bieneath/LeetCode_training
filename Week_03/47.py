# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         if not nums: return []
#         ret = set()
#         l = len(nums)
#         def dfs(curr, rest):
#             if l == len(curr):
#                 ret.add(tuple(curr))
#                 return
#             for i in range(len(rest)):
#                 dfs(curr + [rest[i]], rest[:i] + rest[i+1:])
#         # main
#         dfs([], nums)
#         return list(ret)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for n in nums:
            new_ans = []
            for it in ret:
                for i in range(len(it)+1):
                    new_ans.append(it[:i] + [n] + it[i:])
                    if i < len(it) and n == it[i]: break # 这个判断写起来特别特别考验逻辑思维能力
            ret = new_ans
        return ret