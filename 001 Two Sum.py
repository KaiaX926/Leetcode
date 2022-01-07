# The core idea of my method is to find the rest part of each num in the list that can sum up to the target. 
# If there's not, then pass this num. If there is, return the index.
# Use for loop to fetch the first part and use try and except to find the rest part.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)-1):
        #     x = nums[i]
        #     nums_sec = nums[i+1:]
        #     for j in range(len(nums_sec)):
        #         y = nums_sec[j]
        #         if x + y == target:
        #             return [i,i+j+1]
        L = nums[:]
        
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            L.remove(x)
            try:
                j = L.index(y) + i + 1
            except ValueError:
                continue
            return [i,j]
