# 这题不能无脑死BFS遍历，会超时。比较好的思路就是给每个节点赋予下标
# root是idx，那么root.left=idx*2, root.right=idx*2+1
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        ret = 0
        dq = deque([(root, 0)])
        while dq:
            le, ri = dq[0][1], dq[-1][1]
            ret = max(ret, ri - le + 1)
            sz = len(dq)
            for _ in range(sz):
                node, idx = dq.popleft()
                if node.left:
                    dq.append((node.left, idx * 2))
                if node.right:
                    dq.append((node.right, idx * 2 + 1))
        return ret

# Pythonic版本
# class Solution:
#     def widthOfBinaryTree(self, root: TreeNode) -> int:
#         dq = deque([(0, root)])
#         ret = 0
#         while dq:
#             ret = max(ret, dq[-1][0] - dq[0][0] + 1)
#             dq = [it for idx, node in dq for it in enumerate([node.left, node.right], idx*2) if it[1]]
#         return ret