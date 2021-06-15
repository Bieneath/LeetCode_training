class Solution:
    def swapPairs(self, head: ListNode, k=2) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        fol, pre = dummy, head
        stack = []
        while True:
            for _ in range(k):
                if not pre: break
                stack.append(pre)
                pre = pre.next
            if len(stack) < k: break
            while stack:
                fol.next = stack.pop()
                fol = fol.next
            fol.next = pre
        return dummy.next