class Solution(object):
    def isNumber(self, s):
        try:
            float(s)
        except:
            return False
        return True