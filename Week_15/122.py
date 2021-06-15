class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        gain = fol = 0
        for i in range(1, l):
            gain += max(0, prices[i] - prices[fol])
            fol += 1
        return gain