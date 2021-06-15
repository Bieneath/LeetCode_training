# 贪心算法
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        l = len(nums)
        i = count = 0
        while True:
            n = nums[i]
            max_dis = i + n # 当前nums[i]能跳到的最远距离
            if max_dis >= l - 1:
                return count + 1
            pos = i
            for j in range(i+1, i+1+n):
                if j + nums[j] > max_dis:
                    pos, max_dis = j, j + nums[j]
            i = pos
            count += 1

# DP算法(超时)
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         l = len(nums)
#         dp = [0] * l
#         for i in range(1, l):
#             min_step = float('inf')
#             for j in range(i-1, -1, -1):
#                 if nums[j] + j >= i:
#                     min_step = min(min_step, dp[j]+1)
#             dp[i] = min_step
#         return dp[l-1]