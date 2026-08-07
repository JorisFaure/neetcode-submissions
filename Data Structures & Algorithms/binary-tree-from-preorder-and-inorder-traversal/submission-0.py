# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for index, val in enumerate(inorder) :
            hashmap[val] = index
        self.preorder_index = 0
        def rec(l, r):
            if l > r:
                return None
            root = TreeNode(preorder[self.preorder_index])
            self.preorder_index +=1
            i = hashmap[root.val]
            root.left = rec(l, i - 1)
            root.right = rec(i + 1, r)

            return root
        return rec(0, len(inorder) - 1)


