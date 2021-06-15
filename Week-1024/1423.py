# 滑窗法；左右两个滑窗[:le]与[ri:]，其中le+ri=k
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k >= len(cardPoints): return sum(cardPoints)
        ret = cur = sum(cardPoints[:k])
        for i in range(k-1, -1, -1):
            cur += - cardPoints[i] + cardPoints[-k+i]
            ret = max(ret, cur)
        return ret