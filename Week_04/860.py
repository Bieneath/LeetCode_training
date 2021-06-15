class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for it in bills:
            if 5 == it: five += 1
            elif 10 == it:
                five -= 1
                ten += 1
            # it == 20的情况
            elif ten > 0: # 有10元先用掉10元硬币
                five -= 1
                ten -= 1
            else: five -= 3
            if five < 0: return False
        return True

# class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         dic = {5: 0, 10: 0, 20: 0}
#         for it in bills:
#             if 5 == it: dic[5] += 1
#             if 10 == it:
#                 if dic[5] == 0:
#                     return False
#                 dic[5] -= 1
#                 dic[10] += 1
#             if 20 == it:
#                 if dic[10] >= 1 and dic[5] >= 1:
#                     dic[10] -= 1
#                     dic[5] -= 1
#                     dic[20] += 1
#                 elif dic[5] >= 3:
#                     dic[5] -= 3
#                     dic[20] += 1
#                 else:
#                     return False
#         return True