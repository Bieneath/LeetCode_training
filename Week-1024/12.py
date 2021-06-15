class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        s = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        ret = ''
        for i, v in enumerate(vals):
            ret += num // v * s[i]
            num %= v
        return ret

# class Solution:
#     def intToRoman(self, num: int) -> str:
#         ones = 'IXCM'
#         fives = 'VLD'
#         ret = ''
#         for i in range(4):
#             digit = num % 10
#             num //= 10
#             if 4 == digit:
#                 ret = ones[i] + fives[i] + ret
#             elif 9 == digit:
#                 ret = ones[i] + ones[i+1] + ret
#             else:
#                 ret = digit % 5 * ones[i] + ret
#                 if digit >= 5:
#                     ret = fives[i] + ret
#         return ret