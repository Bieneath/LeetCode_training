class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = i = 0
        for it in s:
            if i == len(g):
                break
            if it >= g[i]:
                i += 1
                count += 1
        return count