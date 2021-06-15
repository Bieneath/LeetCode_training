# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         check = set()
#         dummy = ListNode(None)
#         dummy.next = head
#         fol, pre = dummy, head
#         while pre:
#             if pre.val not in check:
#                 fol.next = pre
#                 fol = pre
#                 check.add(pre.val)
#             pre = pre.next
#         fol.next = None # 一点收尾工作
#         return dummy.next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next # skip the duplicated node
            cur = cur.next
        return head