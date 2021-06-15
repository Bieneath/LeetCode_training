# 递归算法
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def helper(L, R):
            if L and R and L.val == R.val:
                return helper(L.left, R.right) and helper(L.right, R.left)
            return L == R
        return helper(root.left, root.right)

# # BFS迭代算法
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root: return True
#         dq = [root]
#         while dq:
#             layer = []
#             sz = len(dq)
#             for _ in range(sz):
#                 node = dq.pop(0)
#                 if node:
#                     layer.append(node.val)
#                     dq.extend([node.left, node.right])
#                 else:
#                     layer.append('#')
#             if layer != layer[::-1]:
#                 return False
#         return True