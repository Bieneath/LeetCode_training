# # 从叶子节点开始剥洋葱算法；剥的时候要注意批次，一次只能剥当前情况下的所有叶子节点!
# from collections import defaultdict
# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         if n == 1: return [0]
#         tree = defaultdict(set)
#         for a, b in edges:
#             tree[a].add(b)
#             tree[b].add(a)
#         while len(tree) > 2:
#             leaves = {k for k, v in tree.items() if len(v) < 2}
#             for node in leaves:
#                 for it in tree[node]:
#                     tree[it].discard(node)
#                 tree.pop(node)
#         return list(tree.keys())    

# from collections import defaultdict
# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         if n == 1: return [0]
#         tree = defaultdict(set)
#         for a, b in edges:
#             tree[a].add(b)
#             tree[b].add(a)
#         nodes = set(range(n))
#         while len(nodes) > 2:
#             leaves = {node for node in nodes if len(tree[node]) == 1}
#             for node in leaves:
#                 tree[tree[node].pop()].discard(node)
#             nodes -= leaves
#         return list(nodes)

from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        tree = defaultdict(set)
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)
        nodes = set(range(n))
        leaves = {node for node in nodes if len(tree[node]) == 1}
        while len(nodes) > 2:
            new_leaves = set()
            for node in leaves:
                pair = tree[node].pop()
                tree[pair].discard(node)
                if len(tree[pair]) == 1:
                    new_leaves.add(pair)
            nodes -= leaves
            leaves = new_leaves
        return list(nodes)