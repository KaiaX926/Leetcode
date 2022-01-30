# 1. Consider each value as a root (root runs from first to last)
# 2. Now the problem can be broken into root + left of root + right of root (first, root, last)
# 3. Use (first, last) as the key to check if we have built that subtree or not
# 4. Build its left branch (and store the results into DP) if it is not in DP
# 5. Build its right branch (and store the results into DP) if it is not in DP
# 6. Create the root node and take the left/right branch from DP




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}
        return self.helper(1, n, dp)
        
    def helper(self, first, last, dp):
        if first > last:
            return [None]
        trees = []
        for root in range(first, last+1):
            if not (first, root - 1) in dp:
                dp[first, root - 1] = self.helper(first, root-1, dp) # build the left branch and store to DP
            if not (root + 1, last) in dp:
                dp[root + 1, last] = self.helper(root+1, last, dp) # build the right branch and store to DP
            for left in dp[first, root - 1]: # build the left branch
                for right in dp[root+1, last]: # build the right branch
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    trees.append(node)
        return trees
