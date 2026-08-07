# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lca = None

        
        
        def rec(node) :
            if p.val < node.val and q.val < node.val :
                return rec(node.left)
            
            if node.val < p.val and node.val < q.val :
                return rec(node.right)
            else :
                return node
        return rec(root)
        