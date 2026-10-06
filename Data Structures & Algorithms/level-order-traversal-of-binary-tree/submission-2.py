from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root :
            return []

        stack = deque()

        stack.append(root)
        res = []

        while stack :
            level = []
            level_size = len(stack)
            for i in range (level_size) :
                curr = stack.popleft()
                if curr.left :
                    stack.append(curr.left)
                if curr.right :
                    stack.append(curr.right)
                level.append(curr.val)
            res.append(level)
        
        return res




        