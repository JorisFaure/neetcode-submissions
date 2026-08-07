# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def rec(node) :
            if not node :
                return
            
            if node.val < q.val and node.val < p.val :
                return rec(node.right)
            
            if node.val > q.val and node.val > p.val :
                return rec(node.left)
            
            return node
        return rec(root)