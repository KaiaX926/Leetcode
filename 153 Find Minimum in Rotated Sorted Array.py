class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            if nums[left + 1] > nums[left]:
                left += 1
            else:
                return nums[left + 1]
            
            if nums[right - 1] < nums[right]:
                right -= 1
            else:
                return nums[right]
        
        return nums[0]
