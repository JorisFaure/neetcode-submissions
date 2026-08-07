# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Go to the half of the list
        slow = head
        fast = head

        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        print(slow.val)
        #We invert the half right from slow

        prev = None
        curr = slow
        while curr :
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        l1 = head
        l2 = prev

        while l2.next :
            l1.next, l1 = l2, l1.next
            l2.next, l2 = l1, l2.next
        return

        