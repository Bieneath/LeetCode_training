class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        ret = []
        while stack:
            t = stack.pop()
            if isinstance(t, TreeNode):
                stack.extend([t.right, t.left, t.val])
            if isinstance(t, int):
                ret.append(t)
        return ret