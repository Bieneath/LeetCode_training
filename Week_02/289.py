"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 前序遍历也是DFS遍历的一种！
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ret = []
        stack = [root]
        while stack:
            t = stack.pop()
            if isinstance(t, Node):
                stack.extend(t.children[::-1] + [t.val])
                # stack.extend([*t.children[::-1], t.val])
                # for it in t.children[::-1]:
                #     stack.append(it)
                # stack.append(t.val)              
            if isinstance(t, int): ret.append(t)
        return ret