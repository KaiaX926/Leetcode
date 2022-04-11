# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = 0
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def postorder(root):
            if not root: return 0
            k = 0
            if root.val == p.val or root.val == q.val:
                k += 1
            k += postorder(root.left)
            k += postorder(root.right)
            if k == 2:
                self.ans = root
                return 3
            return k

        postorder(root)
        return self.ans
                
