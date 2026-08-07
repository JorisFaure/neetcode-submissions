# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def rec(node, max_val) :
            if not node :
                return
            if node.val >= max_val :
                max_val = node.val
                self.res += 1
            rec(node.left, max_val)
            rec(node.right, max_val)
            return
        rec(root, float('-inf'))
        return self.res