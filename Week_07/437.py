# # stack + DFS迭代，内存撑爆了。
# class Solution:
#     def pathSum(self, root: TreeNode, target: int) -> int:
#         if not root: return False
#         ret = 0
#         stack = [(root, [0])]
#         while stack:
#             node, path = stack.pop()
#             s = path[-1] + node.val
#             for it in path:
#                 if s - it == target:
#                     ret += 1
#             if root.left:
#                 stack.append((root.left, path + [s]))
#             if root.right:
#                 stack.append((root.right, path + [s]))
#         return ret

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        global ret
        ret = 0
        def dfs(root, path):
            global ret
            if not root: return
            s = path[-1] + root.val
            for it in path:
                if s - it == target:
                    ret += 1
            dfs(root.left, path + [s])
            dfs(root.right, path + [s])
        dfs(root, [0])
        return ret