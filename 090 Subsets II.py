class Solution(object):
    def subsetsWithDup(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        
        
        def addition(res,nums):
            repo = res[:]
            if len(nums) == 0:
                return
            
            while len(nums) > 0:
                for item in repo:
                    a = item + [nums[0]]
                    if a not in res:
                        res.append(a)
                nums = nums[1:]
                addition(res,nums)
                return
        
        addition(res,nums)
        return res
        
        
