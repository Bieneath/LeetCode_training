# DP问题如果DP表设置对了，基本就做出了一半。这题dp[c][b]表示当前房子刷成c颜色且有b个街区情况下的最小花费
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = {(0, 0): 0} # 初始化状态：没颜色，0个街区时候0花费
        next_dp = {} # 暂存器
        for i, h in enumerate(houses): # dp表没个house更新一次
            for color in (range(1, n+1) if h == 0 else [h]): # h为0时候可以选n种颜色，否则只能使用h颜色
                for (c, b), v in dp.items():
                    cur_b = b + (c != color) # 与前面的房子颜色不相同时候block+1
                    if cur_b > target: continue
                    fee = v + (cost[i][color-1] if color != h else 0) # 计算粉刷成color颜色需要的花费
                    next_dp[(color, cur_b)] = min(next_dp.get((color, cur_b), math.inf), fee) # 取最小值（最优）计算
            dp, next_dp = next_dp, {} # 每遍历一间房屋更新一次DP表
        optional_cost = [dp[c, b] for c, b in dp if b == target]
        return min(optional_cost) if optional_cost else -1