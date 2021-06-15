# 并查集解法 https://leetcode.com/problems/evaluate-division/discuss/270993/Python-BFS-and-UF(detailed-explanation) 难度EX，尤其是在路费的更新上，想了好久
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = {} # 并查集根节点指向图
        def find(x):
            dest1, cost1 = dic.setdefault(x, (x, 1))
            if x != dest1:
                dest2, cost2 = find(dest1)
                dic[x] = (dest2, cost1*cost2) # 这里要注意，find某种意义上是单向箭头，因此路费通过乘号连接
            return dic[x]
        def union(x, y, cost):
            dx, cx, dy, cy = *find(x), *find(y)
            if not cost:
                return cx/cy if dx == dy else -1.0 # x/dx=cx, y/dy=cy, dx=dy, 求: x/y = cx/cy
            if dx != dy:
                dic[dx] = (dy, cost * cy / cx) # 这一步让dx->dy，也等于求dx/dy。根据菱形公式，x/y=cost, y/dy=cy, x/dx=cx, 求：dx/dy=cost*cy/cx

        # 构建并查集关系图
        for (x, y), cost in zip(equations, values):
            union(x, y, cost)

        return [union(x[0], x[1], 0) if x[0] in dic and x[1] in dic else -1.0 for x in queries] # 如果x[0]或x[1]不在dic中，直接返回-1.0

# # BFS解法，本质上就是先比较好的构建一个图，然后用BFS搜索最短路径 https://leetcode.com/problems/evaluate-division/discuss/88275/Python-fast-BFS-solution-with-detailed-explantion
# # 如何构建图是个技巧活，值得学习
# from collections import defaultdict
# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#         # 构建图
#         dic = defaultdict(list)
#         for (a, b), v in zip(equations, values):
#             dic[a].append((b, v))
#             dic[b].append((a, 1/v))
#         # 写个寻找最短路径的BFS函数
#         def bfs(a, b):
#             if a not in dic or b not in dic:
#                 return -1.0
#             dq, check = [(a, 1.0)], set()
#             while dq:
#                 t, v = dq.pop(0)
#                 if t == b:
#                     return v
#                 check.add(t) # 防止走回头路
#                 for fol, val in dic[t]:
#                     if fol not in check:
#                         dq.append((fol, v*val))
#             return -1.0
#         return [bfs(x[0], x[1]) for x in queries]