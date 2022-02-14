# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check_height(Node: TreeNode) -> int : 

            if not Node : 
                return 0
            
            lft_sub = check_height(Node.left)
            rgt_sub = check_height(Node.right)
            
            if lft_sub == -1 or rgt_sub == -1 or abs(lft_sub - rgt_sub) > 1 : 
                return -1
            return max(lft_sub, rgt_sub) + 1
        
        return check_height(root) != -1
