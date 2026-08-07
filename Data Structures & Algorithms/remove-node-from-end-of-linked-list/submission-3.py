# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0

        begin = head

        while begin :
            begin = begin.next
            l+=1
        if l == 1 :
            return None

        prev = ListNode()
        start = prev
        curr = head
        for i in range(l-n) :
            prev.next = curr
            curr = curr.next
            prev = prev.next

        prev.next = curr.next

        return start.next


        