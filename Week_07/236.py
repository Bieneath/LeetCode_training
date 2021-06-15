# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if root == p or root == q:
            return root
        le = self.lowestCommonAncestor(root.left, p, q)
        ri = self.lowestCommonAncestor(root.right, p, q)
        if le and ri: return root
        if le: return le
        if ri: return ri