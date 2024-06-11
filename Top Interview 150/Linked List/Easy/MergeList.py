class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        curr = dummy
        if list1[curr.val] < list2[curr.val]:
            list1[curr.val]
            curr =  curr.next
        print(list1)
        



s = Solution()
s.mergeTwoLists([1,2,4],[1,3,4])