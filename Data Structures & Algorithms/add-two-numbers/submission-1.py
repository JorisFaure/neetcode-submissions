# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        power_ten = 1
        n_res = 0
        while l1 :
            n_res += (l1.val*power_ten)
            power_ten*=10
            l1 = l1.next
        power_ten = 1
        while l2 :
            n_res += (l2.val*power_ten)
            power_ten*=10
            l2 = l2.next
        
        if n_res == 0 :
            return ListNode()
        
        new_head = ListNode()
        dummy = new_head

        while n_res > 0 :
            dummy.next = ListNode(n_res%10)
            n_res = n_res//10
            dummy = dummy.next
        return new_head.next    
