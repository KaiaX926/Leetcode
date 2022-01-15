class Solution(object):
    def sortColors(self,nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) < 2:
            return nums
        
        if nums[0] > nums[1]: 
            nums[0], nums[1] = nums[1], nums[0]
        
        i = 2
        while i < len(nums):
            for j in range(len(nums[:i])):
                if nums[i] < nums[j]:
                    nums[:i+1] = nums[:j] + [nums[i]] + nums[j:i]
            i += 1
            
        return nums
