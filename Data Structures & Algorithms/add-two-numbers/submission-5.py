# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head_1 = l1
        head_2 = l2

        retenu = 0

        while l1 and l2 :
            s = l1.val + l2.val
            l1.val = (s+retenu)%10
            l2.val = (s+retenu)%10
            if s+retenu >= 10 :
                retenu = 1
            else :
                retenu = 0
            l1 = l1.next
            l2 = l2.next
        
        if not l1 and l2:
            while l2 :
                s = l2.val
                l2.val = (s+retenu)%10
                if s+retenu >= 10 :
                    retenu = 1
                else :
                    retenu = 0
                l2 = l2.next
            head_1 = head_2
        elif not l2 and l1:
            while l1 :
                s = l1.val
                l1.val = (s+retenu)%10
                if s+retenu >= 10 :
                    retenu = 1
                else :
                    retenu = 0
                print(l1.val, retenu,  s+retenu)
                l1 = l1.next
                
        new_head = head_1
        if retenu == 1:
            while head_1.next :
                head_1 = head_1.next
            head_1.next = ListNode(1)
        
        return new_head
        
            