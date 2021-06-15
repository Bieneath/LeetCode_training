class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff, ret = float('inf'), None
        l = len(nums)
        for i in range(l - 2):
            if i > 0 and nums[i-1] == nums[i]: continue
            j, k = i + 1, l - 1
            while j < k:
                S = nums[i] + nums[j] + nums[k]
                if S == target: return S
                if abs(S - target) < diff:
                    diff = abs(S - target)
                    ret = S
                if S > target:
                    while j + 1 < k and nums[k-1] == nums[k]:
                        k -= 1
                    k -= 1
                elif S < target:
                    while j < k - 1 and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
        return ret