class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxi = 0
        for i in range(1,len(nums)):
            maxi = max(maxi,nums[i] - nums[i-1])
        return maxi
