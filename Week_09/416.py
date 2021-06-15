# 此题为DP中的背包问题
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        cs = sum(nums)
        if cs % 2: return False
        target = cs >> 1
        dp = {0}
        for n in nums:
            if n > target:
                break
            dp |= {n + it for it in dp}
            if target in dp:
                return True
        return False