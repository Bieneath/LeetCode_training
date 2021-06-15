class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        l = len(num)
        if l <= k: return '0'
        stack = []
        for c in num:
            while stack and k and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        return ''.join(stack[:-k or None]).lstrip('0') or '0'