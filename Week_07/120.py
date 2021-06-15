class Solution:
    def minimumTotal(self, tr: List[List[int]]) -> int:
        if not tr: return 0
        if len(tr) == 1: return tr[0][0]
        dp = tr[-1].copy()
        for i, it in enumerate(tr[::-1]):
            if i == 0: continue
            for j in range(len(it)):
                dp[j] = it[j] + min(dp[j], dp[j+1])
        return dp[0]