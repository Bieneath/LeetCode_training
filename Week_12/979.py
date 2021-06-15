# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 现在的思路是，先DFS一次二叉树，统计一下每个节点多出或者缺少多少硬币(balance)以及运送金币路途上的损耗(fee)，返回值是当前节点的balance以及全部路途损耗fee
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(root):
            if not root: return 0, 0 # 如果是空节点，返回需要0枚硬币，路程消耗也为0
            left_balance, left_fee = dfs(root.left)
            right_balance, right_fee = dfs(root.right)
            balance = root.val - 1 + left_balance + right_balance # 当前节点还要多少硬币：root.val-1，然后和左右balance计算一下总体balance
            fee = abs(balance) + left_fee + right_fee # 路途损耗永远是正数，当前的balance绝对值+左右路途损耗
            return balance, fee
        return dfs(root)[1]