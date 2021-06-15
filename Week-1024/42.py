class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        le, ri = 0, l - 1
        level = ret = 0
        while le < ri:
            lower = min(height[le], height[ri])
            level = max(level, lower)
            ret += level - lower
            if height[le] <= height[ri]:
                le += 1
            else:
                ri -= 1
        return ret