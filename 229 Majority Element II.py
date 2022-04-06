class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size, maxi, res = {}, len(nums), []
        
        for num in nums:
            if num in size:
                size[num] += 1
            else:
                size[num] = 1
            
            if size[num] > maxi/3 and num not in res:
                res.append(num)
        
        return res
