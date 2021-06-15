# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        start = ListNode(None)
        start.next = head
        slow, fast = start, head
        path = []
        while True:
            for _ in range(k):
                if fast:
                    path.append(fast)
                    fast = fast.next
            if len(path) < k: break
            while path:
                slow.next = path.pop()
                slow = slow.next
            slow.next = fast
        return start.next