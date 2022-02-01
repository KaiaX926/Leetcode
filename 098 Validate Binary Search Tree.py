class Solution:
    def isValidBST(self, root):
        def Check(node, lb, ub):         
            if node == None:
                return True
            
            if (node.val <= lb) or (node.val >= ub):
                return False
            
            return Check(node.left, lb, node.val) and Check(node.right, node.val, ub)
        
        return Check(root, -float('inf'), float('inf'))
