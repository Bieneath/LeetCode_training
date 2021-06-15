# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        dq = deque([root])
        ret = [[root.val]]
        layer = []
        while dq:
            node = dq.popleft()
            if node.left:
                layer.append(node.left)
            if node.right:
                layer.append(node.right)
            if not dq and layer:
                ret.append([it.val for it in layer])
                dq = deque(layer)
                layer = []
        return ret[::-1]