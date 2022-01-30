
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self,n):
        def ans(start,end):
            if start>end:
                return [None]
            if end==start:
                return [TreeNode(start)]
            result = []
            for i in range(start,end+1):
                left = ans(start,i-1)
                right = ans(i+1,end)
                for pair in product(left,right):
                    result.append(TreeNode(i,pair[0],pair[1]))
            return result
        return ans(1,n)
        
