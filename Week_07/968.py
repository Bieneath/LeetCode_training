# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/binary-tree-cameras/solution/968-jian-kong-er-cha-shu-di-gui-shang-de-zhuang-ta/
# 由于二叉树最底层节点肯定更多，所以从下向上推到，放弃叶子节点，尽量让叶子节点的父节点安装摄像头，这样摄像头的数量才是最少的
# 而从底向上推导的方法就是后序遍历
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        global ret
        ret = 0
        def dfs(root):
            global ret
            if not root:
                return 2 # 2表示watched状态
            l = dfs(root.left)
            r = dfs(root.right)
            if l*r == 0: # 0表示unwatched，此时当前节点一定要是1(装监视器cam)才能满足条件
                ret += 1
                return 1
            if l == 1 or r == 1:
                return 2
            if l == 2 and r == 2: # 如果左右孩子都被watched那么当前节点可以不放cam也暂时不被watched，而等着被其父节点watch
                return 0
        if dfs(root) == 0:
            ret += 1
        return ret