# # 0-1背包思想贴近总重量的一半值
# class Solution:
#     def lastStoneWeightII(self, stones: List[int]) -> int:
#         su = sum(stones)
#         target = su >> 1
#         dp = {0}
#         for n in stones:
#             dp |= {x+n for x in dp if x+n <= target}
#         m = max(dp)
#         return su - m * 2

# # 0-1背包解法升级版
# class Solution:
#     def lastStoneWeightII(self, stones: List[int]) -> int:
#         su = sum(stones)
#         dp = {0}
#         for n in stones:
#             dp |= {x+n for x in dp}
#         return min(abs(su - 2*x) for x in dp)

# 传统DP算法，遍历stones，stones[0:i]中所有可能的差值
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        for n in stones:
            dp = {n + x for x in dp} | {abs(n - x) for x in dp}
        return min(dp)