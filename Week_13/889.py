# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归算法，参见官方题解，延续105、106的递归+分治思路，相当相当秒，而且容易理解
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root
        L = post.index(pre[1]) + 1 # 通过前序、后续遍历的特性，计算出root的左边有多少节点
        root.left = self.constructFromPrePost(pre[1:1+L], post[:L])
        root.right = self.constructFromPrePost(pre[1+L:], post[L:-1])
        return root

# # 参见 https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/161268/C%2B%2BJavaPython-One-Pass-Real-O(N) 循环版本容易理解一点。核心思路就是两个指针i, j指向pre和post，当pre[i] != post[j]，左边有空插左边，右边有空插入右边，同时用个栈stack记录插入的pre[i]。当pre[i] == post[j]时，弹出栈最后的一个元素，同时j++。一直到stack[-1]!=post[j]，这个过程其实是在模拟树返回父节点的过程。
# class Solution:
#     def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
#         stack = [TreeNode(pre[0])]
#         j = 0
#         for i in range(1, len(pre)):
#             node = TreeNode(pre[i])
#             while stack[-1].val == post[j]:
#                 stack.pop()
#                 j += 1
#             if not stack[-1].left:
#                 stack[-1].left = node
#             elif not stack[-1].right:
#                 stack[-1].right = node
#             stack.append(node)
#         return stack[0]