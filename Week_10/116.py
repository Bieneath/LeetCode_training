# 来自光头哥的优秀代码 https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37484/7-lines-iterative-real-O(1)-space 通过一个.next，将二叉树遍历变成类似一个二维矩阵遍历
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        ret = root
        while root:
            next_layer = root.left
            while root and root.left:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next_layer
        return ret

# # 使用广度优先搜索
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if not root: return None
#         dq = [root]
#         layer = []
#         while dq:
#             node = dq.pop(0)
#             if node.left: layer.append(node.left)
#             if node.right: layer.append(node.right)
#             if not dq:
#                 for i, v in enumerate(layer):
#                     if 0 == i:
#                         pre = v
#                         continue
#                     pre.next = v
#                     pre = pre.next
#                 dq = layer
#                 layer = []
#         return root