# Definition for singly-linked list.
# class ListNode
#     def __init__(self, val=0, next=None)
#         self.val = val
#         self.next = next
class Solution
    def mergeTwoLists(self, l1 ListNode, l2 ListNode) - ListNode
        start = cur = ListNode()
        p1, p2 = l1, l2
        while p1 and p2
            if p1.val  p2.val
                cur.next = p1
                p1 = p1.next
            else
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        cur.next = p1 or p2
        return start.next