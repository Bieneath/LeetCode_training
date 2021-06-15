class Solution:
    def largestRectangleArea(self, hs: List[int]) -> int:
        ret = 0
        stack = [[-1, -1]]
        for i, h in enumerate(hs):
            while stack[-1][1] > h:
                t = stack.pop()
                left = stack[-1][0]
                ret = max(ret, t[1]*(i-left-1))
            stack.append([i, h])
        # 扫尾工作，将stack中剩余值弹出
        i = len(hs)
        while len(stack) > 1:
            t = stack.pop()
            left = stack[-1][0]
            ret = max(ret, t[1]*(i-left-1))
        return ret