# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode] :
        

        def dfs(node, curr) :
            if not curr.left and node.val < curr.val :
                curr.left = node
                return
            if not curr.right and node.val > curr.val :
                curr.right = node
                return
            
            if node.val < curr.val :
                dfs(node, curr.left)
            else :
                dfs (node, curr.right)
            return
        
        newNode = TreeNode(val)
        if not root :
            return newNode

        dfs(newNode, root)

        return root