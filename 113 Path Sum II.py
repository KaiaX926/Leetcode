# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        self.find(root,targetSum,[])
        return self.res
        
    
    def find(self,root,targetSum,curr):
        if root:
            if targetSum - root.val == 0 and not root.left and not root.right:
                self.res.append(curr + [root.val])
                return
            else:
                self.find(root.left,targetSum - root.val,curr + [root.val])
                self.find(root.right,targetSum - root.val,curr + [root.val])
        
        return
    
    
