# 类推到最多删除k个字符，判断是否是回文字符串
class Solution:
    def validPalindrome(self, s: str, k=1) -> bool:
        def helper(s, k):
            le, ri = 0, len(s) - 1
            while le < ri:
                if s[le] != s[ri]:
                    if k == 0: # 如果k已经是0表示不能删除字符，直接返回False
                        return False
                    return helper(s[le:ri], k-1) or helper(s[le+1:ri+1], k-1)
                le, ri = le + 1, ri - 1
            return True
        return helper(s, k)

# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         def isValid(s):
#             return s == s[::-1]
#         le, ri = 0, len(s) - 1
#         while le < ri:
#             if s[le] != s[ri]:
#                 return isValid(s[le:ri]) or isValid(s[le+1:ri+1])
#             le += 1
#             ri -= 1
#         return True