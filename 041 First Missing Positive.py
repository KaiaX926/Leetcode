# The core idea is to check how many positive numbers appear correctly.
# The first missing number is the counts plus one.


class Solution(object):
    def firstMissingPositive(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ct = 1
        for i in range(len(nums)):
            if ct == nums[i]:
                ct += 1
            
        return ct
