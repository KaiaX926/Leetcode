# The core idea is to check whether the current number is equal to the number before. If yes, then drop it and add an underscore at tail. If no, then move one step forward.
# The process ends when there's no more unchekced number in the list or the rest of the list are all underscores.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 2:
            return len(nums)
        
        
        r = [nums[0]]
        head = 1
    
        
        while head < len(nums) and nums[head] != '_':
            if nums[head] != nums[head - 1]:
                head += 1
            else:
                del nums[head]
                nums.append('_')

                
        return head
