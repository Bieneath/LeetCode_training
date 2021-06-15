class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        MIN = float('inf')
        profit = 0
        for p in prices:
            if p < MIN:
                MIN = p
            else:
                profit = max(profit, p - MIN)
        return profit