# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 快慢双指针解法；两个指针pf和ps，时间步为t，pf的初始位置为2，速度为2t；ps初始位置为0，速度为t，这样pf始终
# 领先ps指针2t+2的距离。如果pf探索到列表最后，那么ps的下一个位置就是列表的中间位置。这种探索法，如果列表元素
# 个数为偶数的情况下，“中间”位置为N//2，N为列表元素个数。
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        if not head.next: return TreeNode(head.val)
        ps, pf = head, head.next.next # 构建快慢双指针，快的指针比慢的指针领先2个位置
        while pf and pf.next: # 因为pf要一次移动两个位置，所以要考虑pf.next是否存在
            pf = pf.next.next
            ps = ps.next
        m_point = ps.next
        ps.next = None # 切成前后两段
        root = TreeNode(m_point.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(m_point.next)
        return root