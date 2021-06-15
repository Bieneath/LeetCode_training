# 因为列表变成环状，首节点和末尾节点不能被同时选中，所以可以设计两个循环，
# 从第一个节点开始遍历的正循环和从最后一个节点开始的反向循环。返回值就是两个循环的较大的那个值

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 由于此时首尾相连，所以要算两个循环，一个从nums[0]开始，另一个从nums[-1]开始
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        nums1 = nums[:-1]
        nums2 = nums[1:]
        l = len(nums)-1
        dp = [0] * l
        dp[0] = nums1[0]
        for i in range(1, l):
            if 1 == i: 
                dp[i] = max(nums1[0], nums1[1])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums1[i])
        res = dp[-1]
        dp = [0] * l
        dp[-1] = nums2[-1]
        for i in range(l-2, -1, -1):
            if l-2 == i:
                dp[i] = max(nums2[l-1], nums2[l-2])
            else:
                dp[i] = max(dp[i+1], dp[i+2] + nums2[i])
        return max(res, dp[0])