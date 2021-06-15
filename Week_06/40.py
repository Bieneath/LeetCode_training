# DP算法
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [set() for _ in range(target+1)]
        # dp[0].add(())
        dp[0] = {()}
        candidates.sort()
        for i in candidates:
            if i > target: break
            for j in range(target, i-1, -1):
                for tup in dp[j-i]:
                    dp[j].add(tup + (i,))
        return list(dp[-1])

# 递归算法
# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         dp = [set() for _ in range(target+1)]
#         dp[0].add(()) # 加入一个空的tuple
#         candidates.sort()
#         for i in candidates:
#             if i > target: break
#             for j in range(target, i-1, -1):
#                 for tup in dp[j-i]:
#                     dp[j].add(tup + (i, ))
#         return list(dp[target])