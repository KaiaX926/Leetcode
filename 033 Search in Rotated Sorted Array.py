# The core idea is to recognize whether the list has been rotated first and start searching from both ends of the list.
# If the list has been rotated, ends searching when the number on the left pointer is smaller than the number on the right pointer or the left pointer is larger than the right pointer.
# If no, ends when the left pointer is larger than the right pointer.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        left,right = 0,len(nums) - 1
        
        if nums[0] > nums[-1]:
            while left <= right and nums[left] > nums[right]:
                if target < nums[left] and target > nums[right]:
                    return -1
                elif target < nums[right]:
                    right -= 1
                elif target > nums[left]:
                    left += 1
                elif nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right 
                    
        
        else:
            while left <= right:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                else:
                    left += 1
                    right  -= 1
        
        return -1
