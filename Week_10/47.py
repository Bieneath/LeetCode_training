# # 首先要明白排列的概念，给定数字1, 2, 3，包括的排列有
# # [1, 2, 3] [1, 3, 2] [2, 1, 3] [2, 3, 1] [3, 1, 2] [3, 2, 1]
# # 如下的算法是根据先确定1，再确定2的各个位置，然后再确定3的各个位置。
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         ret = [[]]
#         for n in nums: # 遍历nums作为循环的最外层，也是让整个循环结束的方法
#             new_ans = []
#             for it in ret:
#                 for i in range(len(it) + 1):
#                     new_ans.append(it[:i] + [n] + it[i:])
#                     # 重复的数字只插在前面，因为it[i]这个数字会往后排。
#                     if i < len(it) and n == it[i]:
#                         break
#             ret = new_ans
#         return ret

# 尝试一下回溯递归算法
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 全排列题目中，对nums先进行排序（相同数字归类）非常非常的重要！
        l = len(nums)
        ret = []
        def dfs(path, remain):
            if len(path) == l:
                ret.append(path)
                return
            i = 0
            while i < len(remain):
                if i == 0 or remain[i] != remain[i-1]: # 只有sort后这个判断才有效
                    dfs(path + [remain[i]], remain[:i] + remain[i+1:])
                i += 1
        dfs([], nums)
        return ret