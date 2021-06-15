class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ret = i = s = 0 # ret: return value, s: SUM
        while True:
            if s >= n:
                return ret
            if i < len(nums) and s + 1 >= nums[i]:
                s += nums[i]
                i += 1
            else:
                s += s + 1
                ret += 1