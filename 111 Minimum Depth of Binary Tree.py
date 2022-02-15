# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root):
        steps = 1
        self.res = []
        
        if not root:
            return 0
        
        def find(steps,root):
            if not root.right and not root.left:
                self.res.append(steps)
                return steps - 1
            
            if root.left:
                steps = find(steps + 1,root.left)  #=1
            if root.right:
                steps = find(steps + 1,root.right)
            
            return steps - 1
        
        find(steps,root)
        
        return min(self.res)
