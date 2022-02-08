# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [root]
        self.res = []
        if root:
            self.save(stack)
        
        return self.res
        
    
    
    def save(self,stack):
        temp,stack_next = [],[]
        while stack:
            a = stack.pop()
            temp.append(a.val)
            if a.left:
                stack_next = [a.left] + stack_next
            if a.right:
                stack_next = [a.right] + stack_next
        
        if len(self.res)%2 == 0:
            self.res.append(temp)
        else:
            self.res.append(temp[::-1])
        
        if stack_next:
            self.save(stack_next)
        
        return
