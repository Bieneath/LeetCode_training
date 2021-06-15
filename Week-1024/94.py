# # 使用迭代方法进行中序遍历
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         stack = [root]
#         ret = []
#         while stack:
#             t = stack.pop()
#             if isinstance(t, TreeNode):
#                 stack.extend([t.right, t.val, t.left])
#             elif isinstance(t, int):
#                 ret.append(t)
#         return ret

# Morris中序遍历 Morris中序遍历图解 https://leetcode-cn.com/problems/recover-binary-search-tree/solution/yi-wen-zhang-wo-morrisbian-li-suan-fa-by-a-fei-8/
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        while root:
            if root.left:
                temp = root.left
                while temp.right and temp.right != root:
                    temp = temp.right
                if not temp.right:
                    temp.right, root = root, root.left
                    continue
                # temp.right == root:
                temp.right = None
            ret.append(root.val)
            root = root.right
        return ret