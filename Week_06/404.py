# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 可以对原函数增加一个参数，方便确认是否为左子树
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, isLeft=False) -> int:
        if not root: return 0
        if isLeft and not root.left and not root.right:
            return root.val
        return self.sumOfLeftLeaves(root.left, isLeft=True) + self.sumOfLeftLeaves(root.right)

# # 第一次提交的代码
# class Solution:
#     def sumOfLeftLeaves(self, root: TreeNode) -> int:
#         if not root: return 0
#         global ret
#         ret = 0
#         def dfs(root):
#             global ret
#             if root.left:
#                 if not root.left.left and not root.left.right:
#                     ret += root.left.val
#                 dfs(root.left)
#             if root.right:
#                 dfs(root.right)
#             return
#         dfs(root)
#         return ret