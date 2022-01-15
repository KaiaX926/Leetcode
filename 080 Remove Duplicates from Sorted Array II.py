class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_n = {}
        i = 0
        while i < len(nums):
            if nums[i] not in dict_n:
                dict_n[nums[i]] = 1
            else:
                dict_n[nums[i]] += 1
                
            if dict_n[nums[i]] > 2:
                nums.remove(nums[i])
            else:
                i += 1
        
        return len(nums)
                
            
