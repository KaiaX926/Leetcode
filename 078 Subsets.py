class Solution(object):
    def subsets(self,nums):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        k = len(nums)
        nums.sort()
        if k == 0:
            return []
        
        new,res = [[i] for i in nums],[[i] for i in nums]
        res = self.find(res,new,nums,k-1)
        
        return [[]] + res

    def find(self,res, prefix, nums, k): 
        if k == 0:
            return res
        
        new = []  
        for item in prefix:
            loc = nums.index(max(item))
            for i in nums[loc+1:]:
                a = item[:]
                a.append(i)
                res.append(a)
                new.append(a)
        res = self.find(res, new,nums, k-1)
        return res
        
