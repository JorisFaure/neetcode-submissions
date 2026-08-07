# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.res = True

        def rec(node) :
            if not node :
                return 0

            left = rec(node.left)
            right = rec(node.right)

            if (right-left) * (right-left) > 1 :
                self.res = False

            return 1 + max(left, right)
        rec(root)
        return self.res





