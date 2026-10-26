# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode] :
        

        def dfs(node, curr) :
            if not curr :
                return node
            
            if node.val < curr.val :
                curr.left = dfs(node, curr.left)
            else :
                curr.right = dfs(node, curr.right)
            return curr
        
        newNode = TreeNode(val)

        if not root :
            return newNode

        return dfs(newNode, root)