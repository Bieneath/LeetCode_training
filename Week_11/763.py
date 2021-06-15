# # 使用集合的交集来验证条件"each letter appears in at most one part"方法，想法很巧妙，代码也简单易于理解，但是时间复杂度很糟糕。
# class Solution:
#     def partitionLabels(self, S: str) -> List[int]:
#         ret = []
#         while S:
#             i = 1
#             while set(S[:i]) & set(S[i:]):
#                 i += 1
#             ret.append(i)
#             S = S[i:]
#         return ret

# 贪心+双指针思路的简化版代码
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = {v: i for i, v in enumerate(S)}
        le = ri = 0
        ret = []
        for i, v in enumerate(S):
            ri = max(ri, dic[v])
            if i == ri: # 遇到断层
                ret.append(ri - le + 1)
                le = ri + 1
        return ret

'''
贪心+双指针。首先遍历一遍S，分别找到每个字母的最左边和最右边出现的位置，记录进pos字典。然后再次遍历列表，le先锁定在最左边，ri在最右边，通过i遍历[le, ri]中间的元素，查看是否有元素的有边界大于当前的ri，并更新ri。这里有个技巧，及i遍历[le, ri]时候不能用range，这会导致ri无法及时更新。我用了while i < ri + 1，这样ri就能在循环中实时更新。
'''
# class Solution:
#     def partitionLabels(self, S: str) -> List[int]:
#         if not S: return []
#         pos = {}
#         ret = []
#         for i, v in enumerate(S):
#             if v not in pos:
#                 pos[v] = [i, i]
#             else:
#                 pos[v][1] = i
#         le = 0
#         while le < len(S):
#             ri = pos[S[le]][1]
#             i = le # i从le开始到ri结束。
#             while i < ri + 1:
#                 ri = max(ri, pos[S[i]][1])
#                 i += 1
#             ret.append(ri - le + 1)
#             le = ri + 1 # 让le移动到ri的下一个位置
#         return ret