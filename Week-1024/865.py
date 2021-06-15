# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 一次遍历法 https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/discuss/146808/C%2B%2BJavaPython-One-Pass
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(root): # dfs的返回值为1.最深深度 2.最深的节点
            if not root: return 0, None
            l, r = dfs(root.left), dfs(root.right)
            if l[0] > r[0]: return l[0] + 1, l[1]
            elif l[0] < r[0]: return r[0] + 1, r[1]
            else: return l[0] + 1, root
        return dfs(root)[1]

# class Solution:
#     def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
#         if not root: return None
#         def get_depth(root, depth): # 检测root为根的树的最大深度
#             if not root: return depth
#             return max(get_depth(root.left, depth + 1), get_depth(root.right, depth + 1))
#         def helper(root): # 左右深度相同返回root，不相同则探测更深的半边树
#             left = get_depth(root.left, 0)
#             right = get_depth(root.right, 0)
#             if left == right:
#                 return root
#             else:
#                 return helper(root.left) if left > right else helper(root.right)
#         return helper(root)