class Solution:
    def replaceSpace(self, s: str) -> str:
        ret = ''
        for c in s:
            if c is not ' ': ret += c
            else: ret += '%20'
        return ret