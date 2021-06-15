class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1: return []
        def helper(s, le, ri):
            if len(s) == 2*n:
                ret.append(s)
                return
            if le < n:
                helper(s+'(', le+1, ri)
            if ri < le:
                helper(s+')', le, ri+1)
            return
        ret, s = [], '('
        helper(s, 1, 0)
        return ret