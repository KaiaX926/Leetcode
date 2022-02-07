# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack_l, stack_r = [],[]
        l,r = root,root
        while (l or r) or (stack_l or stack_r):
            while (l or r):
                if not (l and r):
                    return False
                stack_l.append(l)
                stack_r.append(r)
                l = l.left
                r = r.right
            l = stack_l.pop()
            r = stack_r.pop()
            
            if r.val != l.val:
                return False
            
            l = l.right
            r = r.left
        
        return True
            
        
