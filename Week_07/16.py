# 在三数和基础上改
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = float('inf')
        l = len(nums)
        for i in range(l-2):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            j, k = i+1, l-1
            while j < k:
                v = nums[i] + nums[j] + nums[k]
                if v == target:
                    return v
                if abs(target - v) < abs(target - ret):
                    ret = v
                if v < target:
                    while j < k and nums[j] == nums[j+1]: j += 1
                    j += 1
                elif v > target:
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    k -= 1
        return ret