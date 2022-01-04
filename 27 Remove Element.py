# The core idea is to check whether the current number is equal to the target number. If yes, drop it and add an underscore and the end of the list. If no, move one step forward.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # if len(nums) == 0:
        #     return 0
    
        head = 0
    
        while head < len(nums) and nums[head] != '_':
            if nums[head] == val:
                del nums[head]
                nums.append('_')
            else:
                head += 1
    
        return head
