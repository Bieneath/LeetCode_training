# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        # 标准的前序遍历
        pre = TreeNode()
        stack = [root]
        while stack:
            node = stack.pop()
            if not node: continue
            pre.left, pre.right = None, node
            pre = pre.right
            stack.extend([node.right, node.left])
        return root