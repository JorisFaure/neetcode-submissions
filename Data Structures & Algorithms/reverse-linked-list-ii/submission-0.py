# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or head.next == None or left==right:
            return head

        curr = head

        prev = None
        count = 1
        
        #while we are not on left, we keep continuing
        while count < left:
            prev = curr
            curr = curr.next
            count+=1

        #curr = left_node, prev = the node before left, we will keep them intact

        new_prev = curr
        new_curr = curr.next
        
        #We inverse from left to right but without touching to the left.next for now so we directly assigned the prev to curr
        while count < right :
            next_ = new_curr.next
            new_curr.next = new_prev
            new_prev = new_curr
            new_curr = next_
            count+=1
        #when we exit, new_curr is the node at the right of right, new_prev is the right node
        #Rebranch step
        curr.next = new_curr

        if left == 1 :
            return new_prev
        prev.next = new_prev
        return head
            

