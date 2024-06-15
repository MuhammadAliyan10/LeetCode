class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution:
    def rotateRight(self,head, k):
        if not head or not head.next or k == 0:
            return head
    
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1


        k = k % length
        if k == 0:
            return head

        current.next = head 
        steps_to_new_head = length - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head


s =Solution()
head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
print(s.rotateRight(head,2))