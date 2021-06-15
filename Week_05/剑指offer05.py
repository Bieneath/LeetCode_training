class Solution:
    def replaceSpace(self, s: str) -> str:
        ret = ''
        for c in s:
            ret += '%20' if c is ' ' else c
        return ret