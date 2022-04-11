class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        countz = sum(v == 0 for v in nums)
        if sum(v == 0 for v in nums) > 1:
            return [0] * len(nums)
        
        allmulti = 1
        for i in range(len(nums)) : 
            if nums[i] != 0:
                allmulti = allmulti * nums[i]

        if countz == 0:
            return [int(allmulti/i) for i in nums]
        else:
            loc = nums.index(0)
            return [0]*loc + [allmulti] + [0]*(len(nums) - loc - 1)
        
