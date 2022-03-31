class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        for ele in enumerate(nums):
            if self.roundFind(ele[1],ele[0], t, tuple(nums), k):
                return True
        return False
    
        
    @lru_cache()
    def roundFind(self,num, loc, t, nums, k):
        start = max(loc-k,0)
        end = min(len(nums), loc+k+1)
        temp = nums[start:loc] + nums[min(loc+1,end):end]
        for i in temp:
            if i >= num-t and i <= num+t:
                return True
        return False

################################################################################



class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        nums = sorted([(n, i) for i, n in enumerate(nums)])
        print(nums)
        
        for i in range(len(nums)-1):  
            for j in range(i+1, len(nums)):
                if nums[j][0] - nums[i][0] > t:
                    break
                elif abs(nums[j][1] - nums[i][1]) <= k:
                    return True
