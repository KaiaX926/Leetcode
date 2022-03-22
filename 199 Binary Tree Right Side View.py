# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        if root:
            stack = [root]
        else:
            return self.ans
        
        
        def check(stack):
            temp = []
            
            if stack:
                top = stack.pop()
                self.ans.append(top.val)
                if top.right:
                    temp = [top.right] + temp
                if top.left:
                    temp = [top.left] + temp
                while stack:
                    top = stack.pop()
                    if top.right:
                        temp = [top.right] + temp
                    if top.left:
                        temp = [top.left] + temp
            
                check(temp)
            
            return 
                
                
        check(stack)
        return self.ans
        
