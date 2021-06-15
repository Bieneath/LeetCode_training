# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from functools import reduce
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        rev = []
        # 中序遍历记录路径数值
        def dfs(root, path):
            if not root.left and not root.right: # 此时为叶子节点
                rev.append(path + str(root.val))
                return
            path += str(root.val)
            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)
        dfs(root, '')
        return reduce(lambda x, y:x+y, map(int, rev), 0) # reduce(func, iterable, initial)