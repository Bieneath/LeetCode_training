class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1] * l
        ret = 0
        for i in range(l):
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            ret = max(ret, dp[i])
        return ret