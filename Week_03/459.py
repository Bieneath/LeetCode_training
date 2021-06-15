class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for i in range(l//2):
            if l % (i+1): continue
            if s[:i+1] * (l // (i+1)) == s:
                return True
        return False