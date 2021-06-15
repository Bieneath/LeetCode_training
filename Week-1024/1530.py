# 每次返回一个所有叶子节点距离的列表，每次返回距离都要+1
from itertools import product
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if distance < 2: return 0
        count = 0
        def dfs(root):
            nonlocal count
            if not root: return [] # 如果root为None，返回空列表
            if not root.left and not root.right:
                return [1] # 当前节点为叶子节点，返回一个距离为1的节点
            le = dfs(root.left)
            ri = dfs(root.right)
            if le and ri and le[0] + ri[0] <= distance: # 只有左右都有节点且最小距离相加<=distance时才有计算的必要
                count += sum(m + n <= distance for m, n in product(le, ri)) # 这里单纯通过le + ri的距离算合格的对数
            return sorted([x + 1 for x in le + ri if x + 1 < distance]) # 这里做了一个排序，同时剪枝x + 1 >= distance的节点
        dfs(root)
        return count