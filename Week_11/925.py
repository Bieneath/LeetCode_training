# 这题typed基本上要比name长，所以可以设置快慢指针，fast作为typed下标，每次循环+1；slow指向name，满足name[slow] == typed[fast]才+1。
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for c in typed:
            if i < len(name) and c == name[i]:
                i += 1
            elif not (i > 0 and c == name[i-1]):
                return False
        return i == len(name) # 只有当name被遍历完才返回True

# class Solution:
#     def isLongPressedName(self, name: str, typed: str) -> bool:
#         i = j = 0
#         while i < len(name) and j < len(typed):
#             if name[i] != typed[j]:
#                 return False
#             cn = ct = 1
#             while i < len(name)-1 and name[i+1] == name[i]:
#                 i += 1
#                 cn += 1
#             i += 1
#             while j < len(typed)-1 and typed[j+1] == typed[j]:
#                 j += 1
#                 ct += 1
#             j += 1
#             if cn > ct:
#                 return False
#         return i == len(name) and j == len(typed)