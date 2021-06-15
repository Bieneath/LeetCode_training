# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 代码一，代码简洁优美，速度不如代码二。
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2: return
        val = (t1.val if t1 else 0) + (t2.val if t2 else 0)
        node = TreeNode(val)
        node.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        node.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return node

# 代码二，代码虽然长了点，但是可以减少遍历的分支，速度更快
# class Solution:
#     def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
#         if not t1 or not t2:
#             return t1 if t1 else t2
#         cur1, cur2 = t1, t2
#         def dfs(cur1, cur2):
#             cur1.val += cur2.val
#             if cur2.left:
#                 if not cur1.left: 
#                     cur1.left = TreeNode(0)
#                 dfs(cur1.left, cur2.left)
#             if cur2.right:
#                 if not cur1.right:
#                     cur1.right = TreeNode(0)
#                 dfs(cur1.right, cur2.right)
#         dfs(cur1, cur2)
#         return t1