# 确定上下边界的递归算法
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, low, high):
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            return helper(root.left, low, root.val) and helper(root.right, root.val, high)
        return helper(root, float('-inf'), float('inf'))

# # 在方法一的基础上改进(中序遍历一定是个递增序列)
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         if not root: return True
#         stack = [root]
#         ret = []
#         while stack:
#             t = stack.pop()
#             if isinstance(t, TreeNode):
#                 stack += [t.right, t.val, t.left]
#             elif isinstance(t, int):
#                 if ret and t <= ret[-1]: 
#                     return False
#                 ret.append(t)
#         return True

# # 方法一：根据二叉搜索树的中序遍历是递增序列的性质
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         if not root: return True
#         stack = [root]
#         ret = []
#         while stack:
#             t = stack.pop()
#             if isinstance(t, TreeNode):
#                 stack.extend([t.right, t.val, t.left])
#             elif isinstance(t, int):
#                 ret.append(t)
#         if any(x >= y for x, y in zip(ret, ret[1:])):
#             return False
#         return True