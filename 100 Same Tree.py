# The core idea is to use stack and inorder traversal to check whether each points of the binary search tree are equal.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stackp,stackq = [],[]
        while (stackp or stackq) or (p or q):
            while p or q:
                if not (p and q):
                    return False
                stackp.append(p)
                stackq.append(q)
                p = p.left
                q = q.left
            p = stackp.pop()
            q = stackq.pop()
            print('check:',p,q)
            print(p.val,q.val)
            if p.val != q.val:
                print('not equal!')
                return False
            
            p = p.right
            q = q.right
                    
        return True
    
