Depth First Traversals: 
(a) Inorder (Left, Root, Right) : 4 2 5 1 3 
(b) Preorder (Root, Left, Right) : 1 2 4 5 3 
(c) Postorder (Left, Right, Root) : 4 5 2 3 1
https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/


#-----------------------------
class Solution:
    def inorderTraversal(self, root):
        
        ans = []
        
        def inorder(node) : 
            
            if not node : 
                return 
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return ans    
        
        
                
            
            
