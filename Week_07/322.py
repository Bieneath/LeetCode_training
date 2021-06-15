class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for n in range(1, amount+1):
            temp = []
            for k in coins:
                if n-k < 0: continue
                dp[n] = min(dp[n], dp[n-k] + 1)
        return dp[-1] if float('inf') != dp[-1] else -1