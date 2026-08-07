# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSubtree_(root, subRoot):
            if root == None and subRoot == None :
                return True
            if root == None and subRoot != None :
                return False
            if root != None and subRoot == None :
                return False
            if root.val != subRoot.val :
                return False
            left = isSubtree_(root.left, subRoot.left)
            right = isSubtree_(root.right, subRoot.right)
            return left and right
        
        if not root :
            return False

        if root.val == subRoot.val :
            if isSubtree_(root, subRoot) :
                return True
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right