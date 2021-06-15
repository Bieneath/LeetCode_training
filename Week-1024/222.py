# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 详细请查看 https://leetcode.com/problems/count-complete-tree-nodes/discuss/62088/My-python-solution-in-O(lgn-*-lgn)-time
# 这里用到了2个概念，第一个概念是如何算一棵完美二叉树的总节点，比如该完美二叉树有h层，那么最后一层有2^(h-1)个节点，全树总共有2^h-1个节点；第二个概念是通过不断探索左节点，能得知根节点到最左边的叶子节点的深度，假设这个方法叫getDepth。通过getDepth(left)和getDepth(right)得到le和ri，如果le==ri，那么说明至少左子树肯定是一个完美二叉树。如果le>ri，那么说明右子树一定是一个完美二叉树。通过概念一，就能算出左边或者右边完美二叉树的总节点数。
class Solution:
    def get_depth(self, root):
            if not root: return 0
            return self.get_depth(root.left) + 1
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
        if left == right:
            ret = (1 << left) - 1 + self.countNodes(root.right)
        elif left > right:
            ret = (1 << right) - 1 + self.countNodes(root.left)
        return ret + 1