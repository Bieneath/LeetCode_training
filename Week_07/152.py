# 和53题不同，这题DP方程的最优解并不能完全从上一步的最优解得到，因为负负得正的原因，
# 所以每个DP方程不但要保存最优（最大）值，还要保存一个最小值，查看是否会否极泰来
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         if not nums: return 0
#         l = len(nums)
#         ret = nums[0]
#         dp = [[0, 0]] * l
#         dp[0] = [nums[0], nums[0]]
#         for i in range(1, l):
#             t = [nums[i], dp[i-1][0]*nums[i], dp[i-1][1]*nums[i]]
#             dp[i] = [min(t), max(t)]
#             ret = max(ret, dp[i][1])
#         return ret

# 参看https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC%2B%2BPython-it-can-be-more-simple 的解法
class Solution:
    def maxProduct(self, A: List[int]) -> int:
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] = (A[i-1] or 1) * A[i]
            B[i] = (B[i-1] or 1) * B[i]
        return max(A + B)