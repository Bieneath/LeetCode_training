# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        dq = deque([(root, 1)])
        while dq:
            node, level = dq.popleft()
            if not node: continue
            if not node.left and not node.right: # 此时node是叶子节点
                return level
            dq.append((node.left, level+1))
            dq.append((node.right, level+1))