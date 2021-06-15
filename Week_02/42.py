class Solution:
    def trap(self, h: List[int]) -> int:
        water = level = 0
        le, ri = 0, len(h)-1
        while le < ri:
            level = max(level, min(h[le], h[ri]))
            if h[le] <= h[ri]:
                water += max(0, level - h[le])
                le += 1
            else:
                water += max(0, level - h[ri])
                ri -= 1
        return water