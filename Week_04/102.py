# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 逐层遍历及BFS，用双向队列
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        dq = deque([root])
        ret = [[root.val]]
        layer = []
        while dq:
            node = dq.popleft()
            if node.left:
                layer.append(node.left)
            if node.right:
                layer.append(node.right)
            if not dq and layer: # 判断一下layer是否为空，防止在ret中加入空列表
                ret.append([it.val for it in layer])
                dq = deque(layer)
                layer = []
        return ret