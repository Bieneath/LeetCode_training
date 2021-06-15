# 视频解法 https://www.bilibili.com/video/BV15v411t7v2?t=189
from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # 构建图
        g = defaultdict(set)
        for a, b in connections:
            g[a].add(b)
            g[b].add(a)
        ret = []
        # tarjan算法部分
        check = [-1] * n # 会被时常更新，用来记录最短路径长
        def dfs(v, par, depth):
            check[v] = depth
            for it in g[v]:
                if it == par: continue
                elif check[it] == -1: # it点还未被访问过
                    check[v] = min(check[v], dfs(it, v, depth+1))
                else: # check[it] != -1
                    check[v] = min(check[v], check[it])
            if check[v] == depth and v != 0: # check[v] == depth表示v的子节点并不能返回比当前depth更小的值，说明后面是一方通行
                ret.append([par, v])
            return check[v] # 经过不停的刷新下限，返回v的最短路径
        dfs(0, -1, 0)
        return ret

# # 并查集方法（超时）
# class Solution:
#     def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
#         def find(x, f):
#             if x != f.setdefault(x, x):
#                 f[x] = find(f[x], f)
#             return f[x]
#         def check(idx=None, f={}, total=n):
#             for i, (x, y) in enumerate(connections):
#                 if i == idx: continue
#                 f[find(y, f)] = find(x, f)
#             return len(f) < total or sum(x == f[x] for x in f) > 1 # 返回True表示idx边是关键连接
#         ret = []
#         for i, v in enumerate(connections):
#             if check(idx=i, f={}):
#                 ret.append(v)
#         return ret
