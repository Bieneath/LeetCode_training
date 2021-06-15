# 循环迭代法
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        stack = [root]
        while stack:
            node = stack.pop()
            if not node: continue
            stack += [node.left, node.right] # 先正常遍历
            node.left, node.right = node.right, node.left # 后翻转左右子节点
        return root

# # 递归法
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if not root: return None
#         left = self.invertTree(root.left)
#         right = self.invertTree(root.right)
#         root.left, root.right = right, left
#         return root