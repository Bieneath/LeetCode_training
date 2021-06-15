# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 利用前序遍历结果分割中序遍历，分治算法
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder: return None
        val = preorder.pop(0)
        idx = inorder.index(val)
        cur = TreeNode(val=val)
        cur.left = self.buildTree(preorder, inorder[:idx])
        cur.right = self.buildTree(preorder, inorder[idx+1:])
        return cur