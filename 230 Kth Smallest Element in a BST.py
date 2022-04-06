# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        
        def traversal(root):
            if root:
                self.res.append(root.val)
                traversal(root.left)
                traversal(root.right)
            return
        
        traversal(root)
        self.res.sort()
        return self.res[k-1]
        
