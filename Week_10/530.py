# class Solution:
#     def getMinimumDifference(self, root: TreeNode) -> int:
#         stack = [root]
#         ret = float('inf')
#         pre = None
#         while stack:
#             t = stack.pop()
#             if isinstance(t, TreeNode):
#                 stack.extend([t.right, t.val, t.left])
#             if isinstance(t, int):
#                 if pre is not None:
#                     ret = min(ret, t - pre)
#                 pre = t
#         return ret

# Pythonic中序遍历解法
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        temp = []
        def dfs(root):
            if root.left: dfs(root.left)
            temp.append(root.val)
            if root.right: dfs(root.right)
        dfs(root)
        return min(b - a for a, b in zip(temp, temp[1:]))