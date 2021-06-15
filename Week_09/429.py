"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# pythonic的递归写法
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        ret = []
        layer = [root]
        while layer:
            ret.append([node.val for node in layer])
            layer = [child for node in layer for child in node.children]
        return ret

# # 利用list记录每一层节点并进行遍历
# class Solution:
#     def levelOrder(self, root: 'Node') -> List[List[int]]:
#         if not root: return []
#         ret = []
#         dq = [root]
#         layer = []
#         temp = []
#         while dq:
#             node = dq.pop(0)
#             temp.append(node.val)
#             for it in node.children:
#                 layer.append(it)
#             if not dq:
#                 ret.append(temp)
#                 temp = []
#                 if layer:
#                     dq = layer
#                     layer = []
#         return ret