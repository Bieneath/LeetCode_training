# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, ret = [root], []
        while stack:
            t = stack.pop()
            if isinstance(t, TreeNode):
                stack.extend([t.right, t.left, t.val])
            elif isinstance(t, int):
                ret.append(t)
        return ret