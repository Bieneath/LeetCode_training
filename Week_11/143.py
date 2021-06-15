# 这题如果想要使用O(1)的空间和O(1.5N)的时间复杂度解决此题，就得结合
# 876和206题，分三步：1.找到中间点，2.反转后半段的链表，3.结合两个链表
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head: return None
        # 1.找到中间节点
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 这里要先让slow.next设置为None，同时让slow走到下一个节点，保证前半段>=后半段，为第三步合并做准备
        l2 = slow.next
        slow.next = None
        # 2.反转后半段的链表
        rev, cur = None, l2
        while cur:
            rev, rev.next, cur = cur, rev, cur.next
        t1, t2 = head, rev
        # 3.合并两个链表
        while t1 and t2:
            next_t1 = t1.next
            next_t2 = t2.next
            t1.next = t2
            t1 = next_t1
            t2.next = t1
            t2 = next_t2
        return

# # 方法二：使用列表保存所有节点，然后进行列表操作。
# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         if not head: return None
#         path = []
#         cur = head
#         while cur:
#             path.append(cur)
#             cur = cur.next
#         i, j = 0, len(path)-1
#         flag = 1 # 控制当前循环动左边还是动右边
#         while i < j:
#             if 1 == flag:
#                 path[i].next = path[j]
#                 i += 1
#                 flag = -1
#             elif -1 == flag:
#                 path[j].next = path[i]
#                 j -= 1
#                 flag = 1
#             path[i].next = None # 收尾，此时i==j，将path最中间的元素.next设置为None。
#         return