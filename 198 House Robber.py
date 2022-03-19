class Solution:
    def rob(self, nums: List[int]) -> int:
	    @cache
	    def helper(index):
		    if index >= len(nums):
			    return 0
		    if index == len(nums) - 1:
			    return nums[-1]
		    return max(helper(index + 2) + nums[index], helper(index + 1))


	    return helper(0)
        
