# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        l = ListNode()
        res = l

        while list1 != None and list2 != None :
            if list1.val <= list2.val :
                l.next = list1
                list1 = list1.next
            else :
                l.next = list2
                list2 = list2.next
            l = l.next
        
        if list1 == None :
            l.next = list2
        else :
            l.next = list1
        return res.next
        