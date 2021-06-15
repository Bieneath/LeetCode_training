# # https://leetcode.com/problems/frog-jump/discuss/193816/Concise-and-fast-DP-solution-using-2D-array-instead-of-HashMap-with-text-and-video-explanation.
# # 下面方法的高效版，使用set查询再快速，也需要log(n)的时间复杂度，现在将set改成bool类型的列表；实际运行下来速度和用set方法差不多！
# class Solution:
#     def canCross(self, stones: List[int]) -> bool:
#         l = len(stones)
#         # dp行对应每个stones元素，列表示当前可用的跳跃步长有哪些；根据题意，第一点步长为1，第二点能获得的最长步长为2，第n点为n，因此行长只要给l+1的长度。
#         dp = [[False] * (l+1) for _ in range(l)]
#         dp[0][1] = True
#         max_step = 1
#         for i in range(1, l):
#             for j in range(i-1, -1, -1):
#                 dis = stones[i] - stones[j]
#                 if dis > max_step: break
#                 if dp[j][dis]:
#                     dp[i][dis-1] = dp[i][dis] = dp[i][dis+1] = True
#                     max_step = max(max_step, dis+1)
#         return any(dp[-1])

# 爬楼梯的变形，dp元素为一个集合，记录从当前为止能选择的跳越步长
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        l = len(stones)
        dp = [set() for _ in range(l)] 
        dp[0].add(1)  # 初始状态dp[0] = 1，只能跳1个步长
        max_step = 1 # 用一个max_step记录已知最长步长，加速j的反向搜索。
        for i in range(1, l):
            for j in range(l-1, -1, -1):
                dis = stones[i] - stones[j]
                if dis > max_step: break # 当dis距离超过已知的最长步长，可以停止j继续往左侧探索
                if dis in dp[j]:
                    dp[i].update([dis-1, dis, dis+1]) # 如果在dp[i]左边的dp元素中有和dis相等的步长，更新dp[i]
                    max_step = max(max_step, dis+1) # 更新已知的最长步长
        return dp[-1] != set()

# # 另一个方法，在当前i点的基础上，为后面能到的点更新step值
# from collections import defaultdict
# class Solution:
#     def canCross(self, stones: List[int]) -> bool:
#         l = len(stones)
#         dp = [set() for _ in range(l)] # 此处不能使用[set()] * l的初始化方式！
#         dp[0].add(1)
#         for i in range(l):
#             for step in dp[i]:
#                 if step == 0: continue
#                 dst = stones[i] + step
#                 if dst in stones:
#                     idx = stones.index(dst)
#                     dp[idx].update([step-1, step, step+1])
#         return dp[-1] != set() # dp[-1]为空就是无法跳到最后一个点