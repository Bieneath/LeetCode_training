class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            t = []
            for c in coins:
                if i-c >= 0: t.append(dp[i-c]+1)
            if t: dp[i] = min(t)
        print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1