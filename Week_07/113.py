# recursion 1: 正常递归
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        ret = []
        def dfs(root, S, path):
            if not root: return
            S += root.val
            if S == target and not root.left and not root.right:
                ret.append(path + [root.val])
                return
            dfs(root.left, S, path + [root.val])
            dfs(root.right, S, path + [root.val])
        dfs(root, 0, [])
        return ret

# recursion 2: 反(fan)常(ren)人(lei)思维的递归算法；算法很有趣，在递归回收时候将当前的root.val添加到头部
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root: return []
        if target == root.val and not root.left and not root.right:
            return [[root.val]]
        temp = self.pathSum(root.left, target - root.val) + self.pathSum(root.right, target - root.val)
        return [[root.val] + it for it in temp]

# BFS + queue
from collections import deque
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root: return []
        ret = []
        dq = deque([(root, 0, [])])
        while dq:
            node, s, path = dq.popleft()
            if target == (s + node.val) and not node.left and not node.right:
                ret.append(path + [node.val])
            if node.left:
                dq.append((node.left, s + node.val, path + [node.val]))
            if node.right:
                dq.append((node.right, s + node.val, path + [node.val]))
        return ret

# DFS + stack
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root: return []
        ret = []
        stack = [(root, 0, [])]
        while stack:
            node, s, path = stack.pop()
            if target == s + node.val and not node.left and not node.right:
                ret.append(path + [node.val])
            if node.left:
                stack.append((node.left, s + node.val, path + [node.val]))
            if node.right:
                stack.append((node.right, s + node.val, path + [node.val]))
        return ret