# BFS时候需要从根课程开始遍历，逐渐扩散到所有课程；与DFS不同，BFS加了一个indegree参数，代表还有多少前置课程未被选修
# 只有当indegree=0时候，当前课程才能被选修！！！
from collections import defaultdict, Counter, deque
class Solution:
    def findOrder(self, N: int, pres: List[List[int]]) -> List[int]:
        dic, indegree = defaultdict(set), Counter()
        for u, v in pres:
            dic[v].add(u)
            indegree[u] += 1
        seq = []
        # 最开始初始化的时候取indegree为0的课程
        dq = deque([x for x in range(N) if indegree[x] == 0])
        # 这里有个很有趣的地方，这题如果条件中出现闭环，就应该返回[]，这个入度的参数设计，确保了只有入度为0的课程才能拓展新的课程
        # 如果拓扑图中有闭环，那么这个闭环里的课程是永远不会出现入度为0的情况，最后也不会被加入seq中！因此最后只要判断一下seq长度。
        while dq:
            c = dq.popleft()
            seq.append(c)
            for nxt in dic[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    dq.append(nxt)
        return seq if len(seq) == N else []

# 这题很难入手，因为判断能否学完的隐藏条件是遍历过程中不能出现环，DFS算法就从是否有环入手
# 如果有环就返回False；外面的大循环是range(N)
# DFS
from collections import defaultdict, deque
class Solution:
    def findOrder(self, N: int, pres: List[List[int]]) -> List[int]:
        dic = defaultdict(set)
        for u, v in pres:
            dic[u].add(v)
        seq = []
        check = [0] * N # check有三种状态，0表示未被遍历过；1表示正则遍历中；2表示已近遍历完成(已经达成选课条件)
        def dfs(i):
            if check[i] == 1: return False
            if check[i] == 2: return True
            check[i] = 1
            for nxt in dic[i]:
                if not dfs(nxt): return False
            # 只有遍历完i的所有前置课程，且都没有返回False情况（即i的前置课程都已能被选修），i才能被选修！！！
            check[i] = 2
            seq.append(i)
            return True
        for i in range(N):
            if not dfs(i):
                return []
        return seq