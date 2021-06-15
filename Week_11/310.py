# 核心思想：其实这题就是找多叉树的中心点，根据无环图的定义，中心点最多不会超过2（3个中心点就会形成环）
# 参考 https://leetcode.com/problems/minimum-height-trees/discuss/76132/Iterative-remove-leaves-Python-solution # 的代码
from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        dic = defaultdict(set)
        for u, v in edges:
            dic[u].add(v)
            dic[v].add(u)
        nodes = set(range(n))
        while len(nodes) > 2:
            leaves = set(i for i in nodes if len(dic[i]) == 1)
            for node in leaves:
                for pair_node in dic[node]: # 因为dic的values是集合，集合无法直接取出元素，所以不能写成dic[dic[node]].discard(node)
                    dic[pair_node].discard(node)
            nodes -= leaves
        return list(nodes)

# 直接BFS会超时
# from collections import defaultdict
# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         ret, m_dep = [], float('inf')
#         dic = defaultdict(set)
#         for u, v in edges:
#             dic[u].add(v)
#             dic[v].add(u)
#         def bfs(root):
#             check = [1] * n
#             check[root] = 0
#             dep = 1
#             layer = [root]
#             next_layer = []
#             while layer:
#                 t = layer.pop(0)
#                 for it in dic[t]:
#                     if check[it]:
#                         next_layer.append(it)
#                         check[it] = 0
#                 if not layer and next_layer:
#                     layer = next_layer
#                     next_layer = []
#                     dep += 1
#             return dep
#         for i in range(n):
#             dep = bfs(i)
#             if dep < m_dep:
#                 m_dep = dep
#                 ret = [i]
#             elif dep == m_dep:
#                 ret.append(i)
#         return ret