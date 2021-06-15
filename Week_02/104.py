# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# BFS: 使用双向队列deque进行广度优先搜索
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        dq = deque([(root, 1)])
        depth = 0
        while dq:
            node, level = dq.popleft()
            if node:
                depth = max(depth, level)
                dq.append((node.left, level+1))
                dq.append((node.right, level+1))
        return depth
# DFS: 使用stack进行广度优先搜索
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         stack = [(root, 1)]
#         depth = 0
#         while stack:
#             node, level = stack.pop()
#             if node:
#                 depth = max(depth, level)
#                 stack.append((node.left, level+1))
#                 stack.append((node.right, level+1))
#         return depth