class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = len(h)
        le, ri = 0, l - 1
        water = level = 0
        while le < ri:
            level = max(level, min(h[le], h[ri]))
            water = max(water, (ri - le)*level)
            if h[le] <= h[ri]:
                le += 1
            else:
                ri -= 1
        return water