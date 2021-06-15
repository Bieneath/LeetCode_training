# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(node, depth):
            if not node:
                return depth
            le = check(node.left, depth+1)
            ri = check(node.right, depth+1)
            if le == -1 or ri == -1 or abs(le - ri) > 1:
                return -1
            else:
                return max(le, ri)
        ret = check(root, 0)
        return ret != -1