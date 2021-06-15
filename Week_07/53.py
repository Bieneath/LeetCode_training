# 使用动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MAX = CUR = float('-inf')
        for n in nums:
            CUR = max(CUR + n, n) # 每个nums[i]都有两个选择，继承前面的子串还是单独另起一个子串
            MAX = max(MAX, CUR)
        return MAX