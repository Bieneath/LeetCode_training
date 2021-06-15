class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1
        l = len(nums)
        dp = [1] * l
        ret = float('-inf')
        for i in range(1, l):
            j = i
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ret = max(ret, dp[i])
        return ret