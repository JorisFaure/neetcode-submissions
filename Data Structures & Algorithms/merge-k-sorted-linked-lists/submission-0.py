# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        output = ListNode()
        count = 0

        for sub in lists :
            heapq.heappush(heap, (sub.val, count, sub))
            count+=1
        
        res = output
        while heap :
            _, _, next_elt = heapq.heappop(heap)
            output.next = next_elt
            if next_elt.next :
                count+=1
                heapq.heappush(heap, (next_elt.next.val, count, next_elt.next))
                
            output = output.next
        return res.next
            

        