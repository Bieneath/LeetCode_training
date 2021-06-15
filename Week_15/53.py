class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MAX = CUR = float('-inf')
        for n in nums:
            CUR = max(CUR + n, n) # 要注意求的是连续子串，连续体现在当前的nums[i]只能接在上个dp[i-1]上或者从自己开始另起炉灶，而不能被“跨过”。
            MAX = max(MAX, CUR)
        return MAX

# # 使用动态规划
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         MAX = CUR = float('-inf')
#         for n in nums:
#             CUR = max(CUR + n, n) # 每个nums[i]都有两个选择，继承前面的子串还是单独另起一个子串
#             MAX = max(MAX, CUR)
#         return MAX