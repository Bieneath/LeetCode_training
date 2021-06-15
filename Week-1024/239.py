from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ret = []
        for i, v in enumerate(nums):
            if dq and i - dq[0] >= k:
                dq.popleft()
            while dq and v >= nums[dq[-1]]: # 这里写>=是为了尽可能保留下标靠后的元素，比如a1=3,a2=3，那么尽可能保留a2，因为a2更新。
                dq.pop()
            dq.append(i)
            if i >= k-1:
                ret.append(nums[dq[0]])
        return ret

# from collections import deque
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         ret = []
#         dq = deque([])
#         for i, v in enumerate(nums):    
#             while dq and nums[dq[-1]] < v:
#                 dq.pop()
#             dq.append(i)
#             if dq[0] == i - k:
#                 dq.popleft()
#             if i >= k-1:
#                 ret.append(nums[dq[0]])
#         return ret

# from collections import deque
# class Solution:
#     def maxSlidingWindow(self, n: List[int], k: int) -> List[int]:
#         ret = []
#         dq = deque([0]) # 维护一个双向队列，内容为元素 下 标！
#         # 将前k个元素插入dq队列中
#         for i in range(1, k):
#             while dq and n[dq[-1]] <= n[i]: 
#                 dq.pop()
#             dq.append(i)
#         print(dq)
#         ret.append(n[dq[0]])
#         # 将剩余的元素插入dq中
#         for i in range(k, len(n)):
#             if dq[0] == i - k: dq.popleft() # 当窗口长为k时，i-k就是划出的元素下标
#             while dq and n[dq[-1]] <= n[i]:
#                 dq.pop()
#             dq.append(i)
#             ret.append(n[dq[0]])
#         return ret