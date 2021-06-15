# 这题可以用栈来解决
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

# # 递归算法
# class Solution:
#     def removeDuplicates(self, S: str) -> str:
#         for i in range(len(S) - 1):
#             if S[i] == S[i+1]:
#                 return self.removeDuplicates(S[:i] + S[i+2:])
#         return S