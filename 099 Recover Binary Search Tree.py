import sys

class Solution(object):
    def __init__(self):
        self.prev = TreeNode(-float('inf'))
        
    def recoverTree(self, root):
        two = []
        self.dfs(root, two)
        two[0].val, two[1].val = two[1].val, two[0].val
    
    def dfs(self, node, two):
        if not node:
            return 
        self.dfs(node.left, two)
        
        if not two and self.prev.val > node.val:    
            two.append(self.prev)
            two.append(node)
        elif self.prev.val > node.val:    
            two[1] = node
        self.prev = node
        
        self.dfs(node.right, two)
        return 
