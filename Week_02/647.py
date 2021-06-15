# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         def isValid(st):
#             return st == st[::-1]
#         if not s: return 0
#         table = [1] * len(s)
#         for i in range(1, len(s)):
#             table[i] += table[i-1]
#             j = i - 1
#             while j >= 0:
#                 if isValid(s[j: i+1]): table[i] += 1
#                 j -= 1
#         return table[len(s)-1]
'''
DP算法，参考https://leetcode-cn.com/problems/palindromic-substrings/solution/shou-hua-tu-jie-dong-tai-gui-hua-si-lu-by-hyj8/
table为True的三种情况:
1. 由单个字符组成。
2. 由 2 个字符组成，且字符要相同。
3. 由多于 2 个字符组成，首尾字符相同，且剩余子串是一个回文串。
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 制作一个len(s) x len(s)的表格
        l = len(s)
        count = 0
        table = [[False]*l for _ in range(l)]
        for j in range(l):
            for i in range(j+1):
                if i == j:
                    table[i][j] = True
                    count += 1
                elif j-i == 1 and s[i] == s[j]:
                    table[i][j] = True
                    count += 1
                elif s[i] == s[j] and table[i+1][j-1]:
                    table[i][j] = True
                    count += 1
        return count
                    