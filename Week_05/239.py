from collections import deque
class Solution:
    def maxSlidingWindow(self, n: List[int], k: int) -> List[int]:
        ret = []
        dq = deque([])
        for i, v in enumerate(n):
            while dq and n[dq[-1]] < v:
                dq.pop()
            dq.append(i)
            if dq[0] == i - k:
                dq.popleft()
            if i >= k-1:
                ret.append(n[dq[0]])
        return ret