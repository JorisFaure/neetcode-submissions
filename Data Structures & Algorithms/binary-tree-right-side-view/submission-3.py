# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        queue = deque([root])

        while queue :
            level_size = len(queue)
            last_node = None
            for i in range(level_size) :
                curr = queue.popleft()
                if curr :
                    queue.append(curr.left)
                    queue.append(curr.right)
                    last_node = curr
            if last_node :
                res.append(last_node.val)
        return res



        
        