# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder: return None
        # 前序遍历中，先访问根节点；找到root后就能根据root值在中序遍历中划分出左右两部分
        val = preorder.pop(0)
        ind = inorder.index(val) # 利用index方法，找到val所在的位置下标
        root = TreeNode(val)
        root.left = self.buildTree(preorder, inorder[:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root