# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# from collections import deque
# 这题是BFS求每一层的均值，不在乎遍历顺序
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        stack = [root]
        ret, layer = [], []
        temp, count = 0, 0
        while stack:
            node = stack.pop()
            temp += node.val
            count += 1
            if node.right: layer.append(node.right)
            if node.left: layer.append(node.left)
            if not stack:
                ret.append(0 if count==0 else temp/count)
                temp, count = 0, 0
                if layer:
                    stack = layer
                    layer = []
        return ret
