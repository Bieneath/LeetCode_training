from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs = Counter(s)
        ct = Counter(t)
        for c in ct:
            if c not in cs or ct[c] > cs[c]:
                return c