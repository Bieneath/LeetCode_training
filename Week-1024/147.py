# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head: return None
        start = ListNode(None)
        start.next = head
        cur = head
        while cur.next:
            if cur.val > cur.next.val:
                fol = start
                while cur.next.val > fol.next.val:
                    fol = fol.next
                node = cur.next
                cur.next = node.next
                node.next = fol.next
                fol.next = node
            else:
                cur = cur.next
        return start.next