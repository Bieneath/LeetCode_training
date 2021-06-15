class Solution:
    def maxProfit(self, max_k: int, prices: List[int]) -> int:
        if not prices: return 0
        # 情况一：如果允许的交易次数max_k >= (l-1)//2时候，因为一次交易至少需要两天，所以总交易数不会超过1/2天数，当超过的时候，就和122题一样了。为了节省计算时间，直接沿用了122题o(n)的DP算法。
        def maxProfit_with_inf_trades():
            l = len(prices)
            dp = [0] * l
            for i in range(1, l):
                dp[i] = max(dp[i-1], dp[i-1] + prices[i] - prices[i-1])
            return dp[-1]
        if max_k > len(prices)//2:
            return maxProfit_with_inf_trades()

        # 情况二：如果允许的交易次数max_k < (l-1)//2时候，就真正成了这题的特色部分
        prices = ['#'] + prices
        l = len(prices)
        max_k = min(max_k, (l-1)//2) # 因为一天只能交易一次，max_k交易次数不可能超过总天数，又由于一次交易至少需要两天，所以最多不超过天数的1/2。
        # 构建三维DP表
        dp = [[[0] * 2 for _ in range(max_k+1)] for _ in range(l)]
        for i in range(l):
            for k in range(max_k+1):
                if i == 0 or k == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = float('-inf')
                    continue
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[-1][-1][0]