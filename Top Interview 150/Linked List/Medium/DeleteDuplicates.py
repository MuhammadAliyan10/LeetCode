from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0 , head)
        prev = dummy
        current = head

        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
        
        return dummy.next
     
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")



node = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
S = Solution()
printList(S.deleteDuplicates(node))