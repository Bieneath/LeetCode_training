# # DP + 堆
# import heapq
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         if n == 1: return 1
#         hq = [2, 3, 5]
#         nums = [2, 3, 5]
#         for _ in range(1, n):
#             cur = heapq.heappop(hq)
#             for it in nums:
#                 mul = cur * it
#                 if mul not in hq:
#                     heapq.heappush(hq, mul) 
#         return cur

# # DP + SortedSet
# from sortedcontainers import SortedSet
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         if n == 1: return 1
#         can = SortedSet([2, 3, 5])
#         nums = [2, 3, 5]
#         for _ in range(1, n):
#             cur = can.pop(0)
#             for it in nums:
#                 can.add(cur * it)
#         return cur

# 改进DP思路的算法
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        i2 = i3 = i5 = 0
        for _ in range(1, n):
            n2, n3, n5 = dp[i2]*2, dp[i3]*3, dp[i5]*5
            dp.append(min(n2, n3, n5))
            if dp[-1] == n2: i2 += 1
            if dp[-1] == n3: i3 += 1
            if dp[-1] == n5: i5 += 1
        return dp[-1]