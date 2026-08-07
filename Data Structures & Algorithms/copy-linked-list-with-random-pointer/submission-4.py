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
        node_list = {}
        def create_copy(node) :
            if node == None :
                return None
            new_node = Node(node.val)
            new_node.next = create_copy(node.next)
            new_node.random = None
            node_list[new_node.val] = new_node
            return new_node
        
        new_head = create_copy(head)

        start = new_head

        while new_head :
            if not head.random :
                new_head.random = None
            else :
                new_head.random = node_list[head.random.val]
            
            head = head.next
            new_head = new_head.next
        return start


        

        