class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-float('inf')] + nums + [-float('inf')]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i-1
