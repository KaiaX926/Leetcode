# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         # inorder: left -> root -> right    [9,3,15,20,7] [8,9,10,3,15,20,7]
        
#         # inv : root -> right -> left       [3,20,7,15,9] [3,20,7,15,9,10,8]
#         inv = postorder[::-1]
#         n = len(inorder)
        
#         def find(loc,bound,state):
#             if loc < n:
                
#                 if state == 'right':
#                     if inorder.index(inv[loc]) > bound :
#                         node = TreeNode(inv[loc])
#                     else:
#                         return None
#                 else:
#                     if inv.index(inorder[loc]) < bound :
#                         node = TreeNode(inorder[loc])
#                     else:
#                         return None
                
                
#                 ind_in = inorder.index(inv[loc])
#                 ind_inv = inv.index(inorder[loc])

#                 node.right = find(loc + 1,ind_in,'right')
#                 node.left = find(ind_inv, loc,'left')
            
#             print(node)
            
#             return node
        
#         return find(0,0,'right')
        
        
        
        
class Solution:
    
    def build_tree(self, inorder, postorder):
        
        if(not inorder or not postorder):
            return None
        
        c_root_val = postorder.pop()
        
        c_root = TreeNode(c_root_val)
        
        if(c_root_val in inorder):
        
            pivot = inorder.index(c_root_val)
                       
            c_root.right = self.build_tree(inorder[pivot+1:], postorder)
            c_root.left = self.build_tree(inorder[0:pivot], postorder)
        
        return c_root
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        return self.build_tree(inorder, postorder)
