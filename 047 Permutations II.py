class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return []
        res = []
        self.getpermut(res,nums,0)
        return res
        
    def getpermut(self,res,nums,idx):
        if idx == len(nums):
            if nums not in res:
                res.append(list(nums))
            return res
            
        for i in range(idx,len(nums)):
            nums[i],nums[idx] = nums[idx],nums[i]
            self.getpermut(res,nums,idx + 1)
            nums[i],nums[idx] = nums[idx],nums[i]
                
            
