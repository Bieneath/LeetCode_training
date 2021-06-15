# 这题上手不太好思考，本质还是0-1背包问题以及造桥问题。棘手在找出的时候所有组合数组，即(1, 2)与(2, 1)算两个组合数。dp列表根据0-1背包的经验，设置为range(0, target+1)的列表，而桥的长度就是nums中的数值。需要注意的是，这题通过桥的长度是继承关系。想明白之后题目做起来就很简单。
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [1] + [0] * target
        for i in range(1, target+1):
            for n in nums:
                if i - n < 0: break
                dp[i] += dp[i-n]
        return dp[target]
    
# # 这个DP思路是将0~target作为行，nums作为列，这样的算法速度非常慢
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         dp = [1] + [0] * target
#         for i, v in enumerate(nums, 1):
#             for j in range(v, target+1):
#                 dp[j] = sum(dp[j-x] for x in nums[:i])
#         return dp[target]