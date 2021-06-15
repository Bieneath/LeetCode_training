# 这题用95的思路会超时，只能换个思路，因为只要返回个数，因此可以写个dp表，将0~n树的个数全存起来，然后再使用95题的思路
class Solution:
    def numTrees(self, n: int) -> int:
        if not n: return 0
        dp = [1] #　这里比较特殊，为了编程方便，这里0的位置设置为1
        def helper(start, end):
            ret = 0
            for it in range(start, end+1): # 根据分治的思路，当前it为根的树的个数为left*right
                ret += dp[it-start] * dp[end-it]
            return ret
        # 构建0~n的dp表
        for i in range(1, n+1):
            dp.append(helper(1, i))
        return dp[-1]