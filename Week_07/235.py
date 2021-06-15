# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 因为是搜索二叉树，左小右大，顺着二叉树搜索，分叉点就是近的祖先
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p, q = (p, q) if p.val <= q.val else (q, p)
        def dfs(root, p ,q):
            if p.val <= root.val <= q.val: # 出现分叉情况
                return root
            if p.val <= q.val < root.val:
                t = dfs(root.left, p, q)
            elif root.val < p.val <= q.val:
                t = dfs(root.right, p, q)
            return t
        return dfs(root, p, q)

# # 和236相同的递归算法(这题不推荐，比较慢)
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if not root: return None
#         if root.val == p.val or root.val == q.val:
#             return root
#         le = self.lowestCommonAncestor(root.left, p, q)
#         ri = self.lowestCommonAncestor(root.right, p, q)
#         if le and ri: return root
#         return le or ri