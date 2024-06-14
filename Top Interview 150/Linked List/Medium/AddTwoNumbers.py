
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            print(val1, val2)
            totalSum = val1 + val2 + carry
            carry  = totalSum // 10
            newVal = totalSum % 10
            current.next = ListNode(newVal)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

def print_list(node: Optional[ListNode]):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# Example usage
s = Solution()
list1 = ListNode(1, ListNode(8))
list2 = ListNode(0)
merged_list = s.addTwoNumbers(list1, list2)
print_list(merged_list)


#! Time complexity is O(max(n , m) )
#! Space complexity is O(max(n,m))