# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_depth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxDepth_(root, curr_depth) :
            if not root :
                self.max_depth = max(self.max_depth, curr_depth)
                return
            left = maxDepth_(root.left, curr_depth+1)
            right = maxDepth_(root.right, curr_depth+1)
        maxDepth_(root, 0)
        return self.max_depth