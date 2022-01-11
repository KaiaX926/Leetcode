

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # greedy
        # https://leetcode.com/articles/jump-game/
        length = len(nums)
        begin = length - 1
        for i in reversed(range(length - 1)):
            if i + nums[i] >= begin:
                begin = i
        return not begin
  
  
#----------------------------------------
# "return not"
# If the returncode is 0 then return True
# If the returncode is not 0 then return False.

