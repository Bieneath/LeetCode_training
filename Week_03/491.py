# DFS递归算法
# class Solution:
#     def findSubsequences(self, nums: List[int]) -> List[List[int]]:
#         if not nums: return []
#         def helper(i, s):           
#             if i >= len(nums): # 终止递归条件
#                 if len(s) > 1: ret.add(tuple(s)) # 添加符合条件的substr并去重
#                 return
#             if nums[i] >= s[-1]: 
#                 s.append(nums[i])
#                 helper(i+1, s)
#                 s.pop()
#             helper(i+1, s) # 不管nums[i]大小如何，helper(i+1, s)这步都要执行
#         # main function
#         ret = set()
#         for i in range(len(nums)-1):
#             helper(i+1, [nums[i]])
#         return list(ret)

# DP算法；比起DFS，更加直观。思路为合法的递增子序列存放进dp容器，遍历nums，判断并更新dp；这里因为要用到set去重，所以在list转tuple转set上要花点心思
# class Solution:
#     def findSubsequences(self, nums: List[int]) -> List[List[int]]:
#         if not nums: return []
#         dp = {(nums[0], )} # 这里要注意，不能直接将list转为set；也不能将int直接转为tuple！元组初始化最好不要用set(x)的方法，可能会出现bug。
#         for i in range(1, len(nums)):
#             temp = {(nums[i], )}
#             for s in dp:
#                 if s[-1] <= nums[i]:
#                     temp.add(s + (nums[i], ))
#             dp.update(temp)
#         return [x for x in dp if len(x)>1]

# DP更Pythonic的写法
# class Solution:
#     def findSubsequences(self, nums: List[int]) -> List[List[int]]:
#         if not nums: return []
#         dp = {(nums[0], )} # 这里要注意，不能直接将list转为set；也不能将int直接转为tuple！元组初始化最好不要用set(x)的方法，可能会出现bug。
#         for it in nums[1:]:
#             # dp.update({s + (it, ) for s in dp if s[-1]<=it}) # 可以用下面代替，更pythonic
#             dp |= {s + (it, ) for s in dp if s[-1]<=it}
#             dp.add((it, ))       
#         return [x for x in dp if len(x)>1]

# ???
class Solution:
    def findSubsequences(self, nums):
        subs = {()}
        for num in nums:
            subs |= {sub + (num,)
                    for sub in subs
                    if not sub or sub[-1] <= num}
        return [sub for sub in subs if len(sub) >= 2]