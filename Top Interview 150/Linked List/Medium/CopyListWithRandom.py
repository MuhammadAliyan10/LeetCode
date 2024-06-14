from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
             return None
        mapping = {}

        current =head
        while current:
             mapping[current] = Node(current.val)
             current = current.next
        current = head
        while current:
             mapping[current].next = mapping.get(current.next)
             current = current.next
        current = head
        while current:
             mapping[current].random = mapping.get(current.random)
             current = current.next
        return mapping[head]
           
                 






s = Solution()
head = Node(7,None, Node(13,0, Node(11,4, Node(10,2, Node(1,0)))))
print(s.copyRandomList(head))
        