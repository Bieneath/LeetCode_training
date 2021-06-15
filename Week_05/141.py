# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 快慢指针解法
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        fast = slow = head
        while True:
            slow = slow.next
            if fast.next and fast.next.next:
                fast = fast.next.next
            else: return False
            if fast.val == slow.val:
                return True
        return False