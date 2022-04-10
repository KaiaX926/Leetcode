# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val > max(p.val,q.val):
            
            #Boths are in left subtree
            
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val < min(p.val, q.val):
            
            #Boths are in Right subtree
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            #Boths are in Different Subtree and the current root is the common ancestor
            return root235 Lowest Common Ancestor of a Binary Search Tree
