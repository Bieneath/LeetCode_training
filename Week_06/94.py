# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        ret = []
        while stack:
            t = stack.pop()
            if isinstance(t, TreeNode):
                stack.extend([t.right, t.val, t.left])
            if isinstance(t, int):
                ret.append(t)
        return ret