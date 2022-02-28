# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # returns a list of nums
        def helper(root, path):
            if not root:
                return [0]
            # if we've reached a leaf
            if not root.left and not root.right:
                return [int(path + str(root.val))]
            left_nums = helper(root.left, path + str(root.val))
            right_nums = helper(root.right, path + str(root.val))
            return left_nums + right_nums
        # make sure first node is not 0
        if root.val == 0:
            return sum(helper(root.left, "") + helper(root.right, ""))
        return sum(helper(root, ""))
