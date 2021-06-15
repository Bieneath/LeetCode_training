# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        ret = []
        def visit(root, path):
            # 判断当前节点是否为叶子节点
            if not root.left and not root.right:
                ret.append(path + str(root.val))
                return
            path = path + str(root.val) + '->' 
            if root.left:
                visit(root.left, path)
            if root.right:
                visit(root.right, path)
        visit(root, '')
        return ret