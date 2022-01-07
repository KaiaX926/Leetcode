# The core idea is to find the closest combination by checking each possible combination using for loop.
# To use the least steps, we set one of the three numbers by picking a number in the input list in order and finding the rest two numbers in the rest of the list.
# The key part is to sort the list first to provide the preciser guidance of updating the focused number in the rest list.

class Solution(object):
    def threeSumClosest(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        r = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 1):
            rest = nums[i+1:]
            left,right = 0, len(rest) - 1
            while left < right:
                s = nums[i] + rest[left] + rest[right]
                print(nums[i], rest[left], rest[right])
                if abs(s - target) == 0:
                    return s
                if abs(r - target) > abs(s - target):
                    #print(r,'VS',s)
                    r = s
                if nums[i] + rest[left] + rest[right] - target > 0:
                    right -= 1
                else:
                    left += 1
        
        return r
