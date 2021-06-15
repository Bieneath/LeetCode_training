class Solution:
    def findLongestWord(self, s: str, dic: List[str]) -> str:
        def isSub(word):
            it = iter(s)
            return all(x in it for x in word)
        dic.sort(key=lambda x:(-len(x), x))
        return next(filter(isSub, dic), '') 

# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/discuss/99590/Short-Python-solutions
# class Solution:
#     def findLongestWord(self, s: str, dic: List[str]) -> str:
#         # 使用生成器iter进行是否是子串的判断
#         def isSub(word):
#             it = iter(s)
#             return all(x in it for x in word)# 当在it中找到x返回True，同时生成器指向x的下一个元素。如果遍历完都没找到x返回False
#         dic.sort(key=lambda x:[-len(x), x])
#         for word in dic:
#             if isSub(word):
#                 return word
#         return ''

# class Solution:
#     def findLongestWord(self, s: str, dic: List[str]) -> str:
#         ls = len(s)
#         dic.sort(key=lambda x:(-len(x), x)) # 这步操作是根据长度逆序排列，长度相同情况下根据字典序排列
#         for word in dic: # for循环中是双指针部分。
#             lw = len(word)
#             i = j = 0
#             while i < ls and j < lw:
#                 if s[i] == word[j]:
#                     j += 1
#                 i += 1
#             if j == lw:
#                 return word
#         return ''