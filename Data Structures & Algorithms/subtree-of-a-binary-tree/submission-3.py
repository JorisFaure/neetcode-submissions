# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False
        def isSame(root, subRoot) :
            if not root and not subRoot :
                return True
            
            if root and subRoot and root.val == subRoot.val :
                return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)
            return False
        
        def dfs(root) :
            if not root :
                return
            if root.val == subRoot.val :
                self.res = isSame(root, subRoot)
                if self.res :
                    return
            
            dfs(root.left)
            dfs(root.right)

            return
        
        dfs(root)
        return self.res
            
        