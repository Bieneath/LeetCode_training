# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 建议看官方题解的双指针思路
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return None
        slow = fast = head
        while True:
            if not fast.next or not fast.next.next: # 无环的情况
                return None
            slow = slow.next
            fast = fast.next.next
            if slow is fast: # 表示有环
                break
        # 进入第二阶段，表示肯定有环，利用公式a = c + (n - 1)(b + c)，
        # 此时从head出发一个和slow一样速度的指针later，later会和slow在环的开始处相遇
        later = head
        while True:
            if later is slow:
                return later
            later = later.next
            slow = slow.next
        return None