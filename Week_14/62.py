from itertools import product
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _, i in product(range(1, m), range(1, n)):
            dp[i] += dp[i-1]
        return dp[-1]