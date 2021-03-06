from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        dq = deque([])
        for i, v in enumerate(nums):    
            while dq and nums[dq[-1]] < v:
                dq.pop()
            dq.append(i)
            if dq[0] == i - k:
                dq.popleft()
            if i >= k-1:
                ret.append(nums[dq[0]])
        return ret