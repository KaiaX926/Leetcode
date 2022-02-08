# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            self.depth = 1
        else:
            return 0
        
        stack = [root]
        self.level(stack)
        
        return self.depth
        
    
    
    def level(self,stack):
        x = 0
        stack_next = []
        while stack:
            a = stack.pop()
            if a.left:
                x = 1
                stack_next.append(a.left)
            if a.right:
                x = 1
                stack_next.append(a.right)
        
        self.depth += x
        if stack_next:
            self.level(stack_next)
        
        return 
    
        
        
