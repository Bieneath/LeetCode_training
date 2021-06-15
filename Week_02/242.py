# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         dic1, dic2 = {}, {}
#         for c in s:
#             if c not in dic1: dic1[c] = 1
#             else: dic1[c] += 1
#         for c in t:
#             if c not in dic2: dic2[c] = 1
#             else: dic2[c] += 1
#         return dic1 == dic2

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = Counter(s)
        dic_t = Counter(t)
        return dic_s == dic_t