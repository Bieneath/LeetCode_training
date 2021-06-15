# 参见 https://leetcode.com/problems/super-egg-drop/discuss/158974/C%2B%2BJavaPython-2D-and-1D-DP-O(KlogN)
# dp[m][k]表示使用m步骤和k个鸡蛋能探索的楼层最多多少层
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (K + 1) for _ in range(N + 1)] # 因为m步骤不可能超过楼层总数N，所以可以将N设为m的上限；初始的时候，0次行动0个蛋，只能探索0层
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                # 如果蛋碎，则表示F在当前层的下面，往下探索，探索的楼层数量是剩余m-1次行动以及k-1个蛋的层数dp[m-1][k-1]；
                # 如果蛋不碎，则表示F在当前层的上面，往上探索，探索的楼层数量是剩余m-1次行动以及k个蛋的层数dp[m-1][k]。同时别忘记了当前的这一层
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][k] >= N: break
        return m
