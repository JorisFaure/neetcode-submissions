"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node :
            return None
        oldToNew = {}

        def dfs(node) :
            oldToNew[node] = Node(node.val)

            for neighbor in node.neighbors :
                if neighbor not in oldToNew :
                    oldToNew[node].neighbors.append(dfs(neighbor))
                else :
                    oldToNew[node].neighbors.append(oldToNew[neighbor])
            return oldToNew[node]
        
        return dfs(node)
        