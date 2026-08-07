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
        
        self.valNodeMap = {}
        def constructCopyWithoutRandom(head) :
            if head == None :
                return None
            self.valNodeMap[head.val] = Node(head.val, constructCopyWithoutRandom(head.next), None)
            return self.valNodeMap[head.val]
        newHead = constructCopyWithoutRandom(head)

        save = newHead
        curr = head
        while curr:
            if curr.random == None :
                save.random = None
            else :
                save.random = self.valNodeMap[curr.random.val]
            curr = curr.next
            save = save.next
        return newHead



        