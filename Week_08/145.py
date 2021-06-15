# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        ret = []
        while stack:
            t = stack.pop()
            if isinstance(t, TreeNode):
                stack.extend([t.val, t.right, t.left])
            if isinstance(t, int):
                ret.append(t)
        return ret