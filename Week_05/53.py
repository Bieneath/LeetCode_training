# 使用动态规划，遍历nums，每个nums[i]有两个选择，跟着前面的一起玩，或者自己玩自己的，判断条件是看加上前面后的结果
# 大还是自己单干的结果大
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [0] * len(nums)
        dp[0] = ret = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            ret = max(ret, dp[i])
        return ret

# 使用动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MAX = CUR = float('-inf')
        for n in nums:
            CUR = max(CUR + n, n) # 每个nums[i]都有两个选择，继承前面的子串还是单独另起一个子串
            MAX = max(MAX, CUR)
        return MAX