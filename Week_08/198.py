# 简单的DP问题, 当前节点node[i] = max(node[i-1], node[i-2]+val)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        ret = [0] * len(nums)
        ret[0] = nums[0]
        ret[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            ret[i] = max(ret[i-1], ret[i-2]+nums[i])
        return ret[len(nums)-1]