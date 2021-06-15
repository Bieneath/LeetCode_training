# 这题通过滑窗方法计算出长度为k的窗口能挽回的客户满意人数的最大值，然后用客户一定满意的人数+挽回的最大值就是要的值
# class Solution:
#     def maxSatisfied(self, customers: List[int], grumpy: List[int], k: int) -> int:
#         ret = cur = base = 0
#         for ri in range(len(grumpy)):
#             cur += grumpy[ri]*customers[ri]
#             if ri - k >= 0:
#                 cur -= grumpy[ri-k]*customers[ri-k]
#             ret = max(ret, cur)
#             if not grumpy[ri]: base += customers[ri]
#         return base + ret

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], k: int) -> int:
        redeem = cur = base = 0
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            if g:
                cur += c
            else:
                base += c
            if i - k >= 0:
                cur -= customers[i - k] * grumpy[i - k]
            redeem = max(redeem, cur)
        return base + redeem