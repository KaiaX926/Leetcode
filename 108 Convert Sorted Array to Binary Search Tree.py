# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
 
	    if len(nums) == 0:
		    return None

	    idx = len(nums) // 2
	    middle = TreeNode(nums[idx])
	    middle.left = self.sortedArrayToBST(nums[:idx])
	    if idx + 1 < len(nums):
		    middle.right = self.sortedArrayToBST(nums[idx + 1 :])

	    return middle

            
            
        
