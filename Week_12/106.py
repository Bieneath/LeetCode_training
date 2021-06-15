# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder: return None
        val = postorder.pop()
        index = inorder.index(val)
        root = TreeNode(val)
        # Python传参时，复杂的数据结构是默认传递内存地址
        root.right = self.buildTree(inorder[index+1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        return root