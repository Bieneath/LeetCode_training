# class Solution:
#     def reverseStr(self, s: str, k: int) -> str:
#         ret = ''
#         while s:
#             reverse, remain, s = s[k-1::-1], s[k:2*k], s[2*k:]
#             ret += ''.join(reverse) + ''.join(remain)
#         return ret

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = list(reversed(s[i:i+k]))
        return ''.join(s)