# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # 先中序遍历并将所有节点地址放进一个列表，然后反向遍历列表，node_list[i].val += node_list[i+1].val
        if not root: return None
        node_list = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            node_list.append(root)
            dfs(root.right)
        dfs(root)
        for i in range(len(node_list)-2, -1, -1):
            node_list[i].val += node_list[i+1].val
        return root