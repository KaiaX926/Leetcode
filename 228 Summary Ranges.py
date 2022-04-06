class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        temp = [nums[0], nums[0]]
        
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1] == 1:
                temp[-1] = nums[i] 
            else:
                if temp[0] != temp[-1]:
                    string = str(temp[0]) + '->' + str(temp[-1])
                else:
                    string = str(temp[0])
                res.append(string)
                temp = [nums[i], nums[i]]
                
        if temp[0] != temp[-1]:
            string = str(temp[0]) + '->' + str(temp[-1])
        else:
            string = str(temp[0])
        res.append(string)  
            
        return res
