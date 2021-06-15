# 二维DP算法 https://leetcode.com/problems/profitable-schemes/discuss/154617/C%2B%2BJavaPython-DP
# 这题基本思路不难，类似搭桥问题，计划方案“2人3收益”相当于桥梁，dp[i+3][j+2]的方案数能继承自dp[i][j]通过此方案。但是这题细节方面比较难想。比如这里为什么要反向遍历？原因是当前dp[i][j]需要由dp[i-?][j-?]计算获得，同时这里有个时序性，新的方案要在之前方案实施结果之上计算得出。
class Solution:
    def profitableSchemes(self, n: int, target: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (n + 1) for _ in range(target + 1)]
        dp[0][0] = 1
        for g, p in zip(group, profit):
            for i in range(target, -1, -1):
                for j in range(n - g, -1, -1):
                    dp[min(target, i + p)][j + g] += dp[i][j]
        return sum(dp[target]) % (10**9 + 7)