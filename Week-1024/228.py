# 巧妙方法的变形，利用python列表内存地址的特性，避开[-1]这种写法，代码看上去更精简清晰
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret, r = [], []
        for n in nums:
            if n - 1 not in r: # 这个判断设计非常巧妙
                r = [] # 给r赋新的list内存地址
                ret += r, # 将r拼接到ret上，此时r与ret[-1]内存地址相同
            r[1:] = n,
        return ['->'.join(map(str, x)) for x in ret]

# # 巧妙的方法，使用逗号的特性，将int类型变成可迭代类型
# class Solution:
#     def summaryRanges(self, nums: List[int]) -> List[str]:
#         ret = []
#         for n in nums:
#             if not ret or ret[-1][-1] + 1 != n:
#                 ret += [], # 这句其实和ret.append([])效果一致，不过逼格更高
#             ret[-1][1:] = n, # n,与[n]效果一致，不过经过测试，n,速度更快，这里其实更值得学习的是[1:]的切片技巧，[][1:]是合法的!
#         return ['->'.join(map(str, x)) for x in ret] # 这里利用了map方法的技巧，map(func, iter)，第二个参数时候可迭代参数，map会自动遍历iter

# # 自己写的代码
# class Solution:
#     def summaryRanges(self, nums: List[int]) -> List[str]:
#         if len(nums) < 2: return [str(x) for x in nums]
#         ret = []
#         temp = str(nums[0])
#         for fol, pre in zip(nums[:-1], nums[1:]):
#             if fol + 1 < pre:
#                 if int(temp) != fol:
#                     ret.append(temp + "->" + str(fol))
#                 else:
#                     ret.append(temp)
#                 temp = str(pre)
#         if fol + 1 == pre:
#             ret.append(temp + "->" + str(pre))
#         else:
#             ret.append(temp)
#         return ret