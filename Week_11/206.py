# 参考了 https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space 反转列表的方法，简化了代码。
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        rev, cur = None, head
        while cur:
            rev, rev.next, cur = cur, rev, cur.next
        return rev

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         le, cur = None, head
#         while cur:
#             ri = cur.next
#             cur.next = le
#             le = cur
#             cur = ri
#         return le