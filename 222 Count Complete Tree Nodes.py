# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.s = 0

        def traversal(root):
            if root:
                self.s += 1
                traversal(root.left)
                traversal(root.right)
            return
        
        traversal(root)
        return self.s
