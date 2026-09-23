# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        mid = 0

        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        curr = slow.next
        slow.next = None
        
        while curr :
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        while prev :
            temp1 = prev.next
            temp2 = head.next

            head.next = prev
            prev.next = temp2
            
            prev = temp1
            head = temp2 

        