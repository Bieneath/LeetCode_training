# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         start = ListNode(None)
#         fol, pre = start, head
#         while pre:
#             if not pre.next or pre.val != pre.next.val:
#                 fol.next = pre
#                 fol = fol.next
#             else:
#                 while pre.next and pre.val == pre.next.val:
#                     pre = pre.next
#             pre = pre.next
#         fol.next = None
#         return start.next
    
# 双向队列方法
from collections import deque
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dq = deque()
        skip = None
        while head:
            if head.val != skip:
                if not dq or dq[-1].val != head.val:
                    dq.append(head)
                else:
                    skip = head.val
                    dq.pop()
            head = head.next
        cur = start = ListNode(None)
        while dq:
            cur.next = dq.popleft()
            cur = cur.next
        cur.next = None # 这里一定不要忘记“断后”！
        return start.next