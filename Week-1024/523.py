# 这题很难，正常的前缀和解法都会超时，只有想到让累加和对k取模才能得到不超时解法
# 基于官方的解题方法： https://leetcode-cn.com/problems/continuous-subarray-sum/solution/lian-xu-de-zi-shu-zu-he-by-leetcode/
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1} # 余数: 前缀和下标
        acc = 0
        for i, n in enumerate(nums):
            acc = (acc + n) % k # acc只记录求和对k的模值
            if acc in dic and i - dic[acc] > 1: # 如果当前模值在dic中出现过，说明这两个数的差一定是k的倍数！
                return True
            dic.setdefault(acc, i) # 保留每个模值最先出现的下标位置，而不是更新下标！
        return False

# 基于动态规划算法...其实算不上动态规划，就是基于查表的算法；耗时非常高，不推荐
# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         if len(nums) < 2: return False
#         dp = nums.copy()
#         for l in range(1, len(nums)):
#             for i in range(len(nums)):
#                 if i+l < len(nums):
#                     dp[i] = dp[i] + nums[i+l]
#                     if (k == 0 and dp[i] == 0) or (k != 0 and dp[i]%k == 0):
#                         return True
#         return False

# # 超时
# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         if len(nums) < 2: return False
#         acc = [0]
#         for n in nums:
#             cur = acc[-1] + n
#             acc.append(cur)
#             for i in range(len(acc) - 2): # 这里要-2，具体问什么要打个草稿
#                 if (cur - acc[i]) % k == 0:
#                     return True
#         return False

# # 超时
# from itertools import accumulate
# import operator
# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         acc = [0] + list(accumulate(nums, operator.add))
#         l = len(acc)
#         for le in range(l):
#             for ri in range(le+2, l):
#                 if (acc[ri] - acc[le]) % k == 0:
#                     return True
#         return False