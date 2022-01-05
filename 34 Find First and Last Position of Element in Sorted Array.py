# The core idea is to search for the start location and the end location of the target number by using pointers start from both ends.
# The process ends when the left pointer is larger than the right pointer or the number on the left pointer, is larger than the target or the number on the right pointer is smaller than the target.

class Solution(object):
    def searchRange(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums) == 1 and target == nums[0]:
            return [0,0]
        
        if len(nums) == 0:
            return [-1,-1]
        
        left,right = 0,len(nums)-1
        a,b = -1,-1
        while left <= right and nums[left] <= target and nums[right] >= target:
            # print('location: ',left,right)
            # print(nums[left],nums[right])
            if nums[left] < target:
                left += 1
            if nums[right] > target:
                right -= 1
            if nums[left] == target:
                a = left
            if nums[right] == target:
                b = right
            if a != -1 and b != -1:
                break
        
        return [a,b]
