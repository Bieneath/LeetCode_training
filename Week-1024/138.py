"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        start = Node(head.val)
        dic = {head: start} # 用一个字典记录原节点和复制节点的配对关系；反过来说，如果一个原节点不在dic中，那么也表示该原节点没有复制节点
        while head:
            if head.next:
                if head.next not in dic: # 如果head.next不为空而且没有被复制过
                    dic[head.next] = Node(head.next.val) # 复制head.next，同时将其注册进dic中
                dic[head].next = dic[head.next] # 将新的复制节点给dic[head].next
            if head.random:
                if head.random not in dic: # 如果head.random不为空且没被复制过
                    dic[head.random] = Node(head.random.val) # 复制head.random，同时将其注册进dic中
                dic[head].random = dic[head.random] # 将新的复制节点给dic[head].random
            head = head.next
        return start