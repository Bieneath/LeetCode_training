from collections import deque
class Solution:
    def maxSlidingWindow(self, n: List[int], k: int) -> List[int]:
        ret = []
        dq = deque([0])
        for i in range(1, k):
            while dq and n[dq[-1]] <= n[i]:
                dq.pop()
            dq.append(i)
        ret.append(n[dq[0]])
        for i in range(k, len(n)):
            if i-k == dq[0]: dq.popleft()
            while len(dq) > 0 and n[dq[-1]] <= n[i]:
                dq.pop()      
            dq.append(i)
            ret.append(n[dq[0]])
        return ret