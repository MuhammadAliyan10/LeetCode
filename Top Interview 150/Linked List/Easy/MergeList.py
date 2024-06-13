class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1:ListNode, list2:ListNode)-> ListNode :
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2



s = Solution()
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
merged_list = s.mergeTwoLists(list1, list2)


#! Time complexity is O((n x m) ^ 2)
#! Space complexity is O(n)