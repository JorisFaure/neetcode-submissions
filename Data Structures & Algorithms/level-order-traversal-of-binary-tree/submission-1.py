# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        q = deque()
        
        q.append(root)

        res = []

        while q :
            level = []
            for i in range(len(q)) :
                n = q.popleft()
                level.append(n.val)

                if n.left :
                    q.append(n.left)
                if n.right :
                    q.append(n.right)
            res.append(level)
        
        return res

