# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head

        l = 0
        while start :
            start = start.next
            l+=1

        index_to_del = l - n
        if index_to_del == 0 :
            return head.next
        
        new_start = head
        for i in range(index_to_del - 1) :
            new_start = new_start.next
        new_start.next = new_start.next.next
        return head
        


        

        return head
        