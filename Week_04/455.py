class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        lg, ls = len(g), len(s)
        i = j = count = 0
        while j < ls and i < lg:
            if s[j] >= g[i]:
                j += 1
                i += 1
                count += 1
            else:
                j += 1
        return count