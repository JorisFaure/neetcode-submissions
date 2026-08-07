"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        self.oldToNew = {}
        def constructCopyWithoutRandom(head) :
            if head == None :
                return None
            self.oldToNew[head] = Node(head.val, constructCopyWithoutRandom(head.next), None)
            return self.oldToNew[head]
        newHead = constructCopyWithoutRandom(head)

        save = newHead
        curr = head
        while curr:
            if curr.random == None :
                save.random = None
            else :
                save.random = self.oldToNew[curr.random]
            curr = curr.next
            save = save.next
        return newHead



        