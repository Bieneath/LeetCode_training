class Solution:
    def minimumTotal(self, tr: List[List[int]]) -> int:
        if not tr or not tr[0]: return 0
        l = len(tr)
        dp = tr[-1].copy()
        for row in tr[-2::-1]:
            for j in range(len(row)):
                dp[j] = min(dp[j], dp[j+1]) + row[j]
        return dp[0]