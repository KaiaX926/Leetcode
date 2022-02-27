class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        start,maxi = 1,1
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                start += 1
            elif nums[i] - nums[i-1] == 0:
                pass
            else:
                maxi = max(maxi,start)
                start = 1

        return max(maxi,start)
