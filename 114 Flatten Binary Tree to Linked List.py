# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root
    
        while current:                 
            if current.left:
                left = current.left    #save a copy of left subtree
                right = current.right  #save a copy of right subtree
                current.left = None    #overwritting left subtree with None
                current.right = left   #overwritting right subtree with copy of left subtree
                while left.right:      
                    #iterate down the left subtree (by bringing up the left.right into left) to access the final node that is furthest to the right within it
                    left = left.right  
                left.right = right     
                #now we can add the stored copy of the original right subtree to the furthest right node within the left subtree we brought across
                #essentially looping to get left.right.right.right.right == final righthand node in left subtree, 
                #then doing .right = right to append the other subtree as needed
    
            current = current.right    #repeat by stepping down one to the right
        
        
        
        
        
#         self.list = []
        
#         def find(root):    
#             if root:
#                 self.list.append(TreeNode(root.val))
#                 find(root.left)
#                 find(root.right)
            
#             return
        
#         find(root)
#         lists = self.list[::1]
#         node = TreeNode(lists.pop())
        
#         while lists:
#             node.right = TreeNode(lists.pop())
        
#         return node
        
        
    
    

            
                
