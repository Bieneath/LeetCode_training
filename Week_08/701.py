# 根据二叉搜索树的特点--左小右大，找到val合适的位置再插入；
# 因为涉及到树的节点创建，所以要设置一个慢指针，记录当前节点的父节点
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        slow = fast = root
        while fast:
            slow = fast
            if val < fast.val:
                fast = fast.left
            else:
                fast = fast.right
        fast = TreeNode(val)
        if val < slow.val:
            slow.left = fast
        else:
            slow.right = fast
        return root