# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        new_root = TreeNode(root.val)
        def dfs(root, new_root):
            if root.left:
                new_root.right = TreeNode(root.left.val)
                dfs(root.left, new_root.right)
            if root.right:
                new_root.left = TreeNode(root.right.val)
                dfs(root.right, new_root.left)
            return
        dfs(root, new_root)
        return new_root