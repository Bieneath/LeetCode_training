class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0] + [-math.inf] * (target + 5000)
        for i in range(1, target+1):
            dp[i] = max(dp[i-v]*10 + j for j, v in enumerate(cost, 1))
        return str(max(dp[target], 0))

# from collections import Counter
# import copy
# class Solution:
#     def largestNumber(self, cost: List[int], target: int) -> str:
#         dic = {x: y for x, y in zip(cost, map(str, range(1, 10)))} # 建立cost: num的键值对，同时num取最大值
#         dp = [None] * (target + 1)
#         dp[0] = Counter()
#         def decode(c):
#             if not c: return 0
#             st = reduce(operator.add, [dic[k]*v for k, v in c.items()])
#             sorted_st = sorted(st, reverse=True)
#             return ''.join(sorted_st)
#         for k in dic.keys():
#             for i in range(k, target+1):
#                 if dp[i-k] is None: # 如果dp[i-k]没有值，直接跳过
#                     continue
#                 temp_c = copy.deepcopy(dp[i-k])
#                 temp_c[k] += 1
#                 if int(decode(dp[i])) < int(decode(temp_c)):
#                     dp[i] = temp_c
#         return '0' if dp[target] is None else decode(dp[target])