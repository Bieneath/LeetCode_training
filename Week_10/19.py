# 使用前后指针fol和pre，两者相差n步
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        fol = pre = dummy
        for _ in range(n): 
            pre = pre.next
        while pre and pre.next:
            pre = pre.next
            fol = fol.next
        # 删除倒数第n个节点
        fol.next = fol.next.next
        return dummy.next