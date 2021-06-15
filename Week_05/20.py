class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(', ']': '[', '}': '{'}
        for it in s:
            if it in dic:
                if not stack or dic[it] is not stack.pop():
                    return False
            else: stack.append(it)
        return not stack