class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count, last = 1, 0
        ret = ""
        for i in range(1, len(s)):
            if '(' == s[i]: count += 1
            elif ')' == s[i]: count -= 1
            if count == 0:
                ret = ret + s[last+1: i]
                last = i + 1
        return ret